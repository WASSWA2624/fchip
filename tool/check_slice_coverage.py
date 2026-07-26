"""Verify that every app-ui screen is owned, ordered, and backend-paired.

Enforces the pairing law in .cursor/mandatories.mdc across:
  app-ui/**/screen.json
  frontend/dev-plan/slices/chronology.yaml
  frontend/dev-plan/slices/registry.yaml
  backend/dev-plan/slices/registry.yaml
  frontend/dev-plan/slices/tracker.md

Usage:
    python tool/check_slice_coverage.py

Exits 0 when the registries are consistent, 1 otherwise.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
APP_UI = REPO_ROOT / "app-ui"
CHRONOLOGY = REPO_ROOT / "frontend" / "dev-plan" / "slices" / "chronology.yaml"
FRONTEND_REGISTRY = REPO_ROOT / "frontend" / "dev-plan" / "slices" / "registry.yaml"
BACKEND_REGISTRY = REPO_ROOT / "backend" / "dev-plan" / "slices" / "registry.yaml"
TRACKER = REPO_ROOT / "frontend" / "dev-plan" / "slices" / "tracker.md"

MODULE_DIR = re.compile(r"^\d{2}-[a-z0-9-]+$")
VALID_SLICE_STATUS = {"not-started", "in-progress", "blocked", "done"}
VALID_SCREEN_STATUS = {
    "not-started",
    "ui-fixtures",
    "contract-defined",
    "backend-in-progress",
    "wired",
    "done",
}
VALID_BACKEND_DISP = {"pending", "paired", "none"}
REQUIRED_SCREEN_KEYS = ("route", "roles", "supported_states", "l10n_key_prefix", "phase")

errors: list[str] = []
warnings: list[str] = []


def fail(message: str) -> None:
    errors.append(message)


def warn(message: str) -> None:
    warnings.append(message)


def parse_yaml_sequence(path: Path, key: str) -> list[dict]:
    """Read a top-level YAML sequence block without PyYAML.

    Supports `key:` followed by items with `key: scalar` and `key: [a, b, c]`.
    Inline comments after values are stripped.
    """
    items: list[dict] = []
    current: dict | None = None
    in_block = False
    target = f"{key}:"

    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue

        if not raw.startswith((" ", "\t")):
            in_block = raw.strip() == target
            if not in_block:
                current = None
            continue

        if not in_block:
            continue

        line = raw.strip()
        if line.startswith("- "):
            current = {}
            items.append(current)
            line = line[2:].strip()

        if current is None or ":" not in line:
            continue

        field, _, value = line.partition(":")
        field = field.strip()
        value = value.strip()
        if " #" in value:
            value = value.split(" #", 1)[0].rstrip()

        if value.startswith("[") and value.endswith("]"):
            inner = value[1:-1].strip()
            current[field] = [v.strip().strip("'\"") for v in inner.split(",") if v.strip()]
        else:
            current[field] = value.strip("'\"")

    return items


def discover_screens() -> dict[str, list[str]]:
    """Map each app-ui module directory to its screen folders."""
    found: dict[str, list[str]] = {}
    for module_dir in sorted(APP_UI.iterdir()):
        if not module_dir.is_dir() or not MODULE_DIR.match(module_dir.name):
            continue
        screens = sorted(
            child.name for child in module_dir.iterdir() if (child / "screen.json").is_file()
        )
        found[module_dir.name] = screens

        for child in sorted(module_dir.iterdir()):
            if child.is_dir() and child.name not in screens and not any(child.iterdir()):
                warn(f"empty folder with no screen.json: app-ui/{module_dir.name}/{child.name}")

    return found


def check_screen_json(module: str, screen: str) -> None:
    path = APP_UI / module / screen / "screen.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"{module}/{screen}: unreadable screen.json ({exc})")
        return

    for key in REQUIRED_SCREEN_KEYS:
        if key not in data or data[key] in (None, "", []):
            fail(f"{module}/{screen}: screen.json missing '{key}'")

    expected_route = f"/{module}/{screen}"
    if data.get("route") != expected_route:
        fail(f"{module}/{screen}: route is {data.get('route')!r}, expected {expected_route!r}")

    expected_prefix = f"{module}.{screen}".replace("-", "_")
    if data.get("l10n_key_prefix") != expected_prefix:
        fail(
            f"{module}/{screen}: l10n_key_prefix is "
            f"{data.get('l10n_key_prefix')!r}, expected {expected_prefix!r}"
        )


def check_chronology(disk: dict[str, list[str]], owners: dict[tuple[str, str], str]) -> None:
    if not CHRONOLOGY.is_file():
        fail(f"missing chronology: {CHRONOLOGY}")
        return

    rows = parse_yaml_sequence(CHRONOLOGY, "screens")
    if not rows:
        fail(f"no screens parsed from {CHRONOLOGY}")
        return

    seen: dict[tuple[str, str], str] = {}
    seen_seq: set[str] = set()
    active = 0

    for index, row in enumerate(rows, 1):
        seq = row.get("seq", "")
        module = row.get("module", "")
        screen = row.get("screen", "")
        slice_id = row.get("slice", "")
        status = row.get("status", "")
        backend = row.get("backend", "")
        expected_seq = f"S-{index:03d}"

        if seq != expected_seq:
            fail(f"chronology row {index}: seq is {seq!r}, expected {expected_seq!r}")
        if seq in seen_seq:
            fail(f"chronology duplicate seq {seq}")
        seen_seq.add(seq)

        if status not in VALID_SCREEN_STATUS:
            fail(f"{seq}: status {status!r} is not one of {sorted(VALID_SCREEN_STATUS)}")
        if backend not in VALID_BACKEND_DISP:
            fail(f"{seq}: backend {backend!r} is not one of {sorted(VALID_BACKEND_DISP)}")

        key = (module, screen)
        if module not in disk or screen not in disk.get(module, []):
            fail(f"{seq}: lists {module}/{screen}, which has no screen.json")
        elif key in seen:
            fail(f"{module}/{screen} appears twice in chronology ({seen[key]} and {seq})")
        else:
            seen[key] = seq

        owner = owners.get(key)
        if owner is None:
            fail(f"{seq}: {module}/{screen} has no owning slice in the frontend registry")
        elif owner != slice_id:
            fail(f"{seq}: slice is {slice_id!r}, registry owner is {owner!r}")

        if status in {
            "ui-fixtures",
            "contract-defined",
            "backend-in-progress",
            "wired",
        }:
            active += 1

        if status == "done" and backend not in {"paired", "none"}:
            fail(f"{seq}: status is done but backend is {backend!r} (need paired or none)")

    if active > 1:
        fail(f"chronology has {active} active screens; only one may be in progress")

    for module, screens in disk.items():
        for screen in screens:
            if (module, screen) not in seen:
                fail(f"{module}/{screen} missing from chronology.yaml")


def check_registries(disk: dict[str, list[str]]) -> dict[tuple[str, str], str]:
    frontend = parse_yaml_sequence(FRONTEND_REGISTRY, "slices")
    backend = parse_yaml_sequence(BACKEND_REGISTRY, "slices")

    if not frontend:
        fail(f"no slices parsed from {FRONTEND_REGISTRY}")
        return {}
    if not backend:
        fail(f"no slices parsed from {BACKEND_REGISTRY}")
        return {}

    backend_by_id = {item.get("id"): item for item in backend}
    frontend_ids = {item.get("id") for item in frontend}

    missing_backend = sorted(i for i in frontend_ids - set(backend_by_id) if i)
    if missing_backend:
        fail(f"slices missing from backend registry: {', '.join(missing_backend)}")

    orphan_backend = sorted(i for i in set(backend_by_id) - frontend_ids if i)
    if orphan_backend:
        fail(f"backend slices with no frontend slice: {', '.join(orphan_backend)}")

    owners: dict[tuple[str, str], str] = {}
    tracker_text = TRACKER.read_text(encoding="utf-8") if TRACKER.is_file() else ""
    if not tracker_text:
        fail(f"missing slice tracker: {TRACKER}")

    for item in frontend:
        slice_id = item.get("id", "<unknown>")
        module = item.get("module", "")
        screens = item.get("screens", [])
        status = item.get("status", "")

        if status not in VALID_SLICE_STATUS:
            fail(f"{slice_id}: status {status!r} is not one of {sorted(VALID_SLICE_STATUS)}")

        if module not in disk:
            fail(f"{slice_id}: module directory app-ui/{module} does not exist")
            continue

        for screen in screens:
            if screen not in disk[module]:
                fail(f"{slice_id}: lists {module}/{screen}, which has no screen.json")
                continue
            key = (module, screen)
            if key in owners:
                fail(f"{module}/{screen} owned by both {owners[key]} and {slice_id}")
            else:
                owners[key] = slice_id

        for screen in item.get("deferred_screens", []):
            if screen not in screens:
                fail(f"{slice_id}: deferred screen {screen!r} is not in its screens list")

        try:
            paired = int(item.get("backend_paired", "0"))
        except ValueError:
            fail(f"{slice_id}: backend_paired must be a whole number")
            paired = -1

        if paired < 0 or paired > len(screens):
            fail(f"{slice_id}: backend_paired {paired} is outside 0..{len(screens)}")
        if status == "done" and paired != len(screens):
            fail(
                f"{slice_id}: status is done but only {paired} of "
                f"{len(screens)} screens are paired with a backend"
            )

        backend_id = item.get("backend_slice", "")
        paired_slice = backend_by_id.get(backend_id)
        if paired_slice is None:
            fail(f"{slice_id}: backend_slice {backend_id!r} not found in backend registry")
        elif paired_slice.get("frontend_module") != module:
            fail(
                f"{slice_id}: backend {backend_id} points at module "
                f"{paired_slice.get('frontend_module')!r}, frontend says {module!r}"
            )

        if tracker_text and slice_id not in tracker_text:
            fail(f"{slice_id}: not listed in frontend/dev-plan/slices/tracker.md")

    for item in backend:
        slice_id = item.get("id", "<unknown>")
        status = item.get("status", "")
        if status not in VALID_SLICE_STATUS:
            fail(f"backend {slice_id}: status {status!r} is not one of {sorted(VALID_SLICE_STATUS)}")

    for module, screens in disk.items():
        for screen in screens:
            if (module, screen) not in owners:
                fail(f"{module}/{screen} has no owning slice in the frontend registry")

    return owners


def main() -> int:
    if not APP_UI.is_dir():
        print(f"error: app-ui not found at {APP_UI}", file=sys.stderr)
        return 1

    disk = discover_screens()
    total = sum(len(v) for v in disk.values())

    for module, screens in disk.items():
        for screen in screens:
            check_screen_json(module, screen)

    owners = check_registries(disk)
    check_chronology(disk, owners)

    for message in warnings:
        print(f"warning: {message}")

    if errors:
        print(f"\nslice coverage FAILED with {len(errors)} problem(s):\n", file=sys.stderr)
        for message in errors:
            print(f"  - {message}", file=sys.stderr)
        return 1

    print(
        f"slice coverage OK: {total} screens across {len(disk)} modules, "
        "chronology and registries aligned."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
