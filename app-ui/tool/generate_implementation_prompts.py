#!/usr/bin/env python3
"""Generate IMPLEMENTATION_PROMPT.md for every app-ui screen, component, and layout."""

from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
APP_UI = ROOT / "app-ui"
CHRONOLOGY = ROOT / "frontend" / "dev-plan" / "slices" / "chronology.yaml"
OUT_NAME = "IMPLEMENTATION_PROMPT.md"
INDEX_NAME = "IMPLEMENTATION_PROMPTS.md"

# Common rule blocks referenced in every prompt
RULES_ROOT = [
    "`.cursor/mandatories.mdc`",
    "`.cursor/app-write-up.mdc`",
    "`.cursor/index.mdc`",
]

RULES_FRONTEND_CORE = [
    "`frontend/.cursor/index.mdc`",
    "`frontend/.cursor/scope.mdc`",
    "`frontend/.cursor/product_delivery.mdc`",
    "`frontend/.cursor/feature_workflow.mdc`",
    "`frontend/.cursor/project_structure.mdc`",
    "`frontend/.cursor/architecture.mdc`",
    "`frontend/.cursor/checklists.mdc`",
]

RULES_UI = [
    "`frontend/.cursor/design-system.mdc`",
    "`frontend/.cursor/components.mdc`",
    "`frontend/.cursor/layouts.mdc`",
    "`frontend/.cursor/ui-patterns.mdc`",
    "`frontend/.cursor/ui-workspace.mdc`",
    "`frontend/.cursor/ui-feedback.mdc`",
    "`frontend/.cursor/navigation.mdc`",
    "`frontend/.cursor/accessibility.mdc`",
    "`frontend/.cursor/assets_branding.mdc`",
]

RULES_DATA = [
    "`frontend/.cursor/state_management.mdc`",
    "`frontend/.cursor/data_modeling.mdc`",
    "`frontend/.cursor/network_api.mdc`",
    "`frontend/.cursor/database_strategy.mdc`",
    "`frontend/.cursor/offline_sync.mdc`",
    "`frontend/.cursor/realtime_sync.mdc`",
    "`frontend/.cursor/instant_ui_sync.mdc`",
    "`frontend/.cursor/storage_strategy.mdc`",
]

RULES_SECURITY = [
    "`frontend/.cursor/security.mdc`",
    "`frontend/.cursor/authentication_session.mdc`",
    "`frontend/.cursor/permissions.mdc`",
]

RULES_QUALITY = [
    "`frontend/.cursor/localization_i18n.mdc`",
    "`frontend/.cursor/validation.mdc`",
    "`frontend/.cursor/error_handling.mdc`",
    "`frontend/.cursor/testing.mdc`",
    "`frontend/.cursor/performance.mdc`",
    "`frontend/.cursor/observability.mdc`",
    "`frontend/.cursor/coding_conventions.mdc`",
]

RULES_BACKEND = [
    "`backend/.cursor/index.mdc`",
    "`backend/.cursor/vertical-slice-delivery.mdc`",
    "`backend/.cursor/module-creation.mdc`",
    "`backend/.cursor/api.mdc`",
    "`backend/.cursor/architecture.mdc`",
    "`backend/.cursor/prisma.mdc`",
    "`backend/.cursor/auth-security.mdc`",
    "`backend/.cursor/validation.mdc`",
    "`backend/.cursor/response-format.mdc`",
    "`backend/.cursor/compliance.mdc`",
    "`backend/.cursor/offline-support.mdc`",
    "`backend/.cursor/websockets.mdc`",
    "`backend/.cursor/testing.mdc`",
]

PLAN_REFS = [
    "`frontend/dev-plan/index.md`",
    "`frontend/dev-plan/00-execution-policy.md`",
    "`frontend/dev-plan/24-product-vertical-slices.md`",
    "`frontend/dev-plan/25-slice-execution-playbook.md`",
    "`frontend/dev-plan/slices/chronology.yaml`",
    "`frontend/dev-plan/slices/registry.yaml`",
    "`frontend/dev-plan/slices/tracker.md`",
    "`frontend/dev-plan/slices/TEMPLATE.md`",
    "`backend/dev-plan/P016_slice_pairing.md`",
]


def module_to_feature(module: str) -> str:
    """00-shared → shared; 07-referrals-desk → referrals_desk."""
    body = re.sub(r"^\d+-", "", module)
    return body.replace("-", "_")


def slug_to_pascal(slug: str) -> str:
    return "".join(part.capitalize() for part in slug.replace("_", "-").split("-"))


def dart_feature_paths(module: str, screen: str) -> dict[str, str]:
    feature = module_to_feature(module)
    base = f"frontend/lib/features/{feature}"
    return {
        "feature_root": base,
        "page": f"{base}/presentation/pages/{screen.replace('-', '_')}_page.dart",
        "widgets": f"{base}/presentation/widgets/",
        "state": f"{base}/presentation/state/",
        "domain": f"{base}/domain/",
        "data": f"{base}/data/",
        "repository": f"{base}/domain/repositories/{feature}_repository.dart",
        "tests": f"frontend/test/features/{feature}/",
        "backend_module": f"backend/src/modules/{feature}/",
    }


def dart_component_path(category: str, slug: str) -> dict[str, str]:
    name = slug.replace("-", "_")
    return {
        "shared_file": f"frontend/lib/shared/components/{category}/app_{name}.dart",
        "barrel": "frontend/lib/shared/components/",
        "tests": f"frontend/test/shared/components/{category}/app_{name}_test.dart",
        "goldens": f"frontend/test/shared/components/{category}/goldens/",
    }


def dart_layout_path(slug: str) -> dict[str, str]:
    name = slug.replace("-", "_")
    return {
        "shared_file": f"frontend/lib/shared/layout/app_{name}.dart",
        "barrel": "frontend/lib/shared/layout/",
        "tests": f"frontend/test/shared/layout/app_{name}_test.dart",
        "goldens": f"frontend/test/shared/layout/goldens/",
    }


def load_chronology() -> dict[tuple[str, str], dict]:
    """Parse chronology.yaml without requiring PyYAML."""
    text = CHRONOLOGY.read_text(encoding="utf-8")
    entries: dict[tuple[str, str], dict] = {}
    current: dict | None = None
    for line in text.splitlines():
        if re.match(r"^\s+- seq:\s+", line):
            if current and "module" in current and "screen" in current:
                entries[(current["module"], current["screen"])] = current
            current = {"seq": line.split(":", 1)[1].strip()}
            continue
        if current is None:
            continue
        m = re.match(r"^\s+(module|screen|slice|wave|deferred|status|backend):\s*(.+)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if key == "deferred":
                current[key] = val.lower() == "true"
            else:
                # strip inline comments
                current[key] = val.split("#", 1)[0].strip()
    if current and "module" in current and "screen" in current:
        entries[(current["module"], current["screen"])] = current
    return entries


def list_specimens(folder: Path) -> list[str]:
    names = sorted(p.name for p in folder.glob("*.png"))
    return names


def bullets(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def rules_block(*groups: list[str]) -> str:
    seen: list[str] = []
    for group in groups:
        for item in group:
            if item not in seen:
                seen.append(item)
    return bullets(seen)


def screen_prompt(
    folder: Path,
    module: str,
    screen: str,
    meta: dict,
    chrono: dict | None,
) -> str:
    paths = dart_feature_paths(module, screen)
    specimens = list_specimens(folder)
    route = meta.get("route", f"/{module}/{screen}")
    layout = meta.get("layout", "(undeclared)")
    shells = meta.get("shells", {})
    body = meta.get("body_layouts", {})
    roles = meta.get("roles", [])
    states = meta.get("supported_states", [])
    l10n = meta.get("l10n_key_prefix", f"{module.replace('-', '_')}.{screen.replace('-', '_')}")
    nav = meta.get("navigation", {})
    access = meta.get("access", {})
    phase = meta.get("phase", "mvp")
    title = meta.get("title", screen)
    subtitle = meta.get("subtitle", "")
    kind = meta.get("kind", "screen")

    seq = chrono.get("seq", "unlisted") if chrono else "unlisted"
    slice_id = chrono.get("slice", f"VS-{module.split('-')[0]}") if chrono else f"VS-{module.split('-')[0]}"
    deferred = chrono.get("deferred", False) if chrono else False
    status = chrono.get("status", "not-started") if chrono else "not-started"

    shells_txt = ", ".join(f"`{k}` → `{v}`" for k, v in shells.items()) or "(undeclared)"
    body_txt = ", ".join(f"`{k}` → `{v}`" for k, v in body.items()) or f"`{layout}`"
    roles_txt = ", ".join(f"`{r}`" for r in roles) or "(undeclared)"
    states_txt = ", ".join(f"`{s}`" for s in states) or "`default`"

    primary = nav.get("primary_action", {})
    tabs = nav.get("tabs", [])
    tabs_txt = "; ".join(f"{t.get('label')} → `{t.get('to')}`" for t in tabs) or "(none)"
    primary_txt = (
        f"{primary.get('label')} → `{primary.get('to')}`" if primary else "(none declared)"
    )

    return f"""# Implementation prompt — `{module}/{screen}`

> Paste this whole file into an agent session when implementing this UI. Do not invent a different screen.

## Mission

Implement **{title}** as a production Flutter screen in `frontend/lib`, with maximum reuse of the shared kit, correct responsive behavior from the six mockups, typed domain/data layers, and a **matching backend** in the same atomic chronology unit before starting the next screen.

{f"_Subtitle: {subtitle}_" if subtitle else ""}

## Identity

| Field | Value |
| --- | --- |
| Kind | Screen (`{kind}`) |
| Module | `{module}` |
| Screen slug | `{screen}` |
| Chronology | `{seq}` |
| Slice | `{slice_id}` |
| Phase | `{phase}` |
| Deferred | `{str(deferred).lower()}` |
| Chronology status | `{status}` |
| Route | `{route}` |
| Parent route | `{meta.get("parent_route", "(none)")}` |
| Layout | `{layout}` |
| Body layouts | {body_txt} |
| Shells | {shells_txt} |
| Roles | {roles_txt} |
| Supported states | {states_txt} |
| Localization prefix | `{l10n}` |
| Access policy | {access.get("policy", "RBAC + ABAC + subscription + assigned modules")} |
| Identifier policy | {meta.get("identifier_policy", "Display human_friendly_id only; never expose raw database IDs")} |

## Visual sources (match; do not raster-copy)

Folder: `app-ui/{module}/{screen}/`

Specimens present:

{bullets(f"`{n}`" for n in specimens) if specimens else "- (no PNGs found — stop and regenerate mockups)"}

Also read:

- `app-ui/{module}/README.md`
- `app-ui/00-shared/tokens.json`
- Shared layout specimens for `{layout}` under `app-ui/00-shared/layouts/{layout}/`
- Shared component specimens listed by that layout's `layout.json` `composes` array
- Connected journeys under `app-flows/` (especially `07-navigation.md` and module journeys)

## Target code locations (reuse before create)

| Layer | Path |
| --- | --- |
| Feature root | `{paths["feature_root"]}/` |
| Page | `{paths["page"]}` |
| Widgets (feature-only) | `{paths["widgets"]}` |
| Presentation state | `{paths["state"]}` |
| Domain | `{paths["domain"]}` |
| Data / repository impl | `{paths["data"]}` |
| Repository contract | `{paths["repository"]}` |
| Router entry | `frontend/lib/app/router/` (route must equal `{route}`) |
| Shared layout | `frontend/lib/shared/layout/` (implement/reuse `{layout}`) |
| Shared components | `frontend/lib/shared/components/` |
| Tests | `{paths["tests"]}` |
| Backend module | `{paths["backend_module"]}` |

**Reuse rule:** If a compliant shared widget, layout, repository helper, or route guard already exists, patch it — do not fork a second copy under another name.

## Applicable rules (must follow)

### Product & delivery

{rules_block(RULES_ROOT, RULES_FRONTEND_CORE, PLAN_REFS)}

### UI / UX / structure

{rules_block(RULES_UI)}

### Data, network, sync

{rules_block(RULES_DATA)}

### Security & permissions

{rules_block(RULES_SECURITY)}

### Quality

{rules_block(RULES_QUALITY)}

### Backend pairing

{rules_block(RULES_BACKEND)}

## Actionable implementation plan

Follow `frontend/dev-plan/25-slice-execution-playbook.md` for `{seq}`:

### Phase 0 — Claim the screen

1. Confirm `{seq}` is the next unfinished non-deferred row in `chronology.yaml` (or stop if another screen is already in progress).
2. Set chronology `status` to `ui-fixtures`.
3. Start a tracker block from `frontend/dev-plan/slices/TEMPLATE.md`.

### Phase 1 — Read before coding

4. Treat `screen.json` in this folder as the contract for route, roles, access, layout, shells, states, navigation, and `l10n_key_prefix`.
5. Open all six mockups (mobile/tablet/desktop × light/dark) and note hierarchy, spacing, CTAs, empty regions, and chrome.
6. Resolve `{layout}` and every composed component against `app-ui/00-shared/`.
7. Map navigation:
   - Tabs: {tabs_txt}
   - Primary action: {primary_txt}
   - Access denied → `{nav.get("access_denied", "/00-shared/access-denied")}`
   - Not found → `{nav.get("not_found", "/00-shared/not-found")}`

### Phase 2 — Flutter UI on fixtures (maximum reuse)

8. Register route `{route}` with the access guard for roles {roles_txt}.
9. Compose the page from shared shells + `{layout}` + catalog components. Prefer:
   - `AsyncStateScaffold`, `ResponsivePage`, `AppWorkspace`, `AppListTable`, `AppWorkspaceDetailPanel`, `AppActionPanel` when they fit `ui-workspace.mdc`.
10. Implement **every** supported state: {states_txt}.
11. Add ARB keys under `{l10n}` only — no hard-coded user strings.
12. Verify at `390×844`, `768×1024`, `1440×900` in light and dark.
13. Back with a typed fixture / fake repository; add unit, widget, and golden tests.
14. Place feature-only widgets under `{paths["widgets"]}`; anything reusable across modules must move to `frontend/lib/shared/`.

### Phase 3 — Derive the backend contract from the built UI

15. Walk the UI and fill the derivation table (field → model; filter → query; CTA → `POST …/<action>`; role → permission; forbidden → authz path; offline/conflict → idempotency + version; live region → scoped event; sensitive read → consent + audit).
16. Define the smallest repository interface and DTO shapes. Set chronology `status` to `contract-defined`.
17. Expose **`human_friendly_id` only** — never raw DB IDs in UI or public payloads.

### Phase 4 — Matching backend (same atomic unit)

18. Implement under `{paths["backend_module"]}` per `backend/dev-plan/P016_slice_pairing.md` and backend rules above: Prisma + migration, Zod, repository, service, controller, routes, permissions, consent, audit, events, seeds, tests.
19. Seeds must reproduce every declared UI state.
20. Set chronology `status` to `backend-in-progress`, then `wired` when the real repository replaces fixtures.

### Phase 5 — Wire, prove, close

21. Delete the fake repository unless tests still override it.
22. Prove one real user action end-to-end plus declared failure states.
23. Mark `{seq}` `status: done`, `backend: paired` (or `none` with static evidence only).
24. Update `tracker.md` and both registries; run `python tool/check_slice_coverage.py`.

## Reusability checklist

- [ ] No duplicate button, chip, banner, form field, nav, or feedback widget invented in the feature folder when a shared catalog item exists
- [ ] Layout `{layout}` is a shared layout implementation, not a one-off Scaffold tree
- [ ] Feature widgets accept data via typed props / providers — no embedded API clients in widgets
- [ ] Repository is the only place that talks to the network / local DB for this screen's data
- [ ] Permissions hide unauthorized actions rather than showing disabled dead ends when policy says omit
- [ ] Loading uses logo-based `AppLoadingIndicator` / `AppButton.isLoading` per mandatories
- [ ] Shared multi-user data updates via realtime + instant UI sync helpers

## Done when

- Visual match to specimens across breakpoints and themes (not pixel-perfect raster copy)
- Route, roles, states, layout, shells, and l10n prefix match this folder's `screen.json`
- Real repository wired (or explicit `backend: none` with evidence)
- Cross-stack proof named in the tracker
- `python tool/check_slice_coverage.py` passes for this screen

## Do not

- Skip ahead while an earlier non-deferred chronology screen is unfinished
- Ship fixtures as "done"
- Expose internal database IDs
- Hard-code colors, spacing, typography, or user-facing strings
- Build unused generic backend endpoints
- Copy PNG mockups into `assets/` as the UI implementation
"""


def component_prompt(folder: Path, category: str, slug: str, meta: dict) -> str:
    paths = dart_component_path(category, slug)
    specimens = list_specimens(folder)
    title = meta.get("title", slug)
    purpose = meta.get("purpose", "")
    used_by = meta.get("used_by", [])
    breakpoints = meta.get("breakpoints", ["mobile", "tablet", "desktop"])
    themes = meta.get("themes", ["light", "dark", "system"])
    class_name = f"App{slug_to_pascal(slug)}"

    return f"""# Implementation prompt — shared component `{category}/{slug}`

> Paste this whole file into an agent session when implementing this reusable component.

## Mission

Implement **{title}** as a single reusable Flutter widget in `frontend/lib/shared/components`, matching the six specimens, with no feature business logic, so every FCHIP screen can compose it safely.

{f"_Purpose: {purpose}_" if purpose else ""}

## Identity

| Field | Value |
| --- | --- |
| Kind | Shared component |
| Category | `{category}` |
| Slug | `{slug}` |
| Suggested Dart name | `{class_name}` |
| Used by | {", ".join(f"`{u}`" for u in used_by) if used_by else "(catalog surfaces)"} |
| Breakpoints | {", ".join(f"`{b}`" for b in breakpoints)} |
| Themes | {", ".join(f"`{t}`" for t in themes)} |

## Visual sources

Folder: `app-ui/00-shared/components/{category}/{slug}/`

{bullets(f"`{n}`" for n in specimens) if specimens else "- (no PNGs found)"}

Also read:

- `app-ui/00-shared/components/README.md`
- `app-ui/00-shared/tokens.json`
- `component.json` in this folder

## Target code locations

| Layer | Path |
| --- | --- |
| Widget | `{paths["shared_file"]}` |
| Barrel / exports | `{paths["barrel"]}` |
| Widget tests | `{paths["tests"]}` |
| Goldens | `{paths["goldens"]}` |

If an equivalent shared widget already exists under another name, **extend or rename in place** — do not create a second component for the same job (`frontend/.cursor/components.mdc`).

## Applicable rules

### Product & delivery

{rules_block(RULES_ROOT, ["`frontend/.cursor/index.mdc`", "`frontend/.cursor/project_structure.mdc`", "`frontend/.cursor/architecture.mdc`", "`frontend/.cursor/checklists.mdc`"])}

### UI kit

{rules_block(RULES_UI)}

### Quality & a11y

{rules_block(RULES_QUALITY, ["`frontend/.cursor/multi_platform_input.mdc`", "`frontend/.cursor/platform_guidelines.mdc`"])}

### Permissions note

- Unauthorized actions that wrap this component must not render the action (`frontend/.cursor/permissions.mdc`).
- Components must not embed RBAC logic beyond accepting an `enabled` / visibility flag from the caller.

## Actionable implementation plan

1. Inventory existing `frontend/lib/shared/components/**` for the same job; reuse or patch first.
2. Read all specimens and list variants (size density, emphasis, icon presence, destructive vs normal, dense tablet vs phone).
3. Design a small public API: required data props, optional style flags, callbacks (`onPressed`, `onSelected`), and localization inputs (pass already-localized `String`s or `Text` widgets — do not hard-code copy inside the component unless it is brand chrome owned by the kit).
4. Implement `{class_name}` with:
   - `const` constructor where possible
   - Design tokens only (no raw colors/spacings)
   - Responsive sizing via `frontend/lib/core/responsive/` helpers
   - States: enabled, disabled, loading, error, focused, empty as relevant
   - Semantics / accessibility labels
5. Export from the shared components barrel.
6. Add widget + golden tests for mobile/tablet/desktop × light/dark using the specimens as visual references (not as image assets inside the widget).
7. Replace any feature-local duplicates once this ships.

## Reusability checklist

- [ ] Lives only under `frontend/lib/shared/components/`
- [ ] Contains **no** feature repository calls, routing, or domain rules
- [ ] One component job → one implementation
- [ ] Works in light and dark; scales across breakpoints
- [ ] All user-facing strings come from callers or brand constants already localized
- [ ] Entities shown inside the component use `human_friendly_id` labels only when data-bound

## Backend linkage

Shared presentational components normally need **no backend**. If this component displays live data (status, sync, risk, feeder health), the **screen** that hosts it owns the repository, providers, and pairing — keep this widget dumb and props-driven.

## Done when

- Specimens matched across breakpoints/themes
- Catalog README entry remains accurate
- Tests/goldens pass
- No second parallel widget exists for the same job

## Do not

- Put this under `frontend/lib/features/**`
- Hard-code feature colors or copy
- Embed API clients or Riverpod notifiers inside the widget
- Copy PNG files into the widget tree
"""


def layout_prompt(folder: Path, slug: str, meta: dict) -> str:
    paths = dart_layout_path(slug)
    specimens = list_specimens(folder)
    title = meta.get("title", slug)
    purpose = meta.get("purpose", "")
    composes = meta.get("composes", [])
    surfaces = meta.get("surfaces", [])
    breakpoints = meta.get("breakpoints", ["mobile", "tablet", "desktop"])
    themes = meta.get("themes", ["light", "dark", "system"])
    class_name = f"App{slug_to_pascal(slug)}"

    compose_links = [
        f"`{c}` → `app-ui/00-shared/components/**/{c}/` + `frontend/lib/shared/components/`"
        for c in composes
    ]

    return f"""# Implementation prompt — shared layout `{slug}`

> Paste this whole file into an agent session when implementing this reusable page layout.

## Mission

Implement **{title}** as a reusable responsive layout shell in `frontend/lib/shared/layout`, composed from shared components, so product screens declare `{slug}` in `screen.json` and plug content slots instead of rebuilding chrome.

{f"_Purpose: {purpose}_" if purpose else ""}

## Identity

| Field | Value |
| --- | --- |
| Kind | Shared layout |
| Slug | `{slug}` |
| Suggested Dart name | `{class_name}` |
| Surfaces | {", ".join(f"`{s}`" for s in surfaces) if surfaces else "(see README)"} |
| Breakpoints | {", ".join(f"`{b}`" for b in breakpoints)} |
| Themes | {", ".join(f"`{t}`" for t in themes)} |

## Visual sources

Folder: `app-ui/00-shared/layouts/{slug}/`

{bullets(f"`{n}`" for n in specimens) if specimens else "- (no PNGs found)"}

Also read:

- `app-ui/00-shared/layouts/README.md`
- `layout.json` in this folder
- Specimens for each composed component

## Composes (implement or reuse these first)

{bullets(compose_links) if compose_links else "- (none listed — inspect specimens)"}

## Target code locations

| Layer | Path |
| --- | --- |
| Layout widget | `{paths["shared_file"]}` |
| Layout barrel | `{paths["barrel"]}` |
| Supporting shells | `frontend/lib/shared/layout/` (`ResponsivePage`, `AsyncStateScaffold`, workspace shells) |
| Tests | `{paths["tests"]}` |
| Goldens | `{paths["goldens"]}` |

## Applicable rules

### Product & structure

{rules_block(RULES_ROOT, ["`frontend/.cursor/index.mdc`", "`frontend/.cursor/project_structure.mdc`", "`frontend/.cursor/architecture.mdc`", "`frontend/.cursor/layouts.mdc`", "`frontend/.cursor/ui-workspace.mdc`", "`frontend/.cursor/navigation.mdc`"])}

### UI kit

{rules_block(RULES_UI)}

### Quality

{rules_block(RULES_QUALITY)}

## Actionable implementation plan

1. Confirm whether `{slug}` already maps to an existing shared layout (`ResponsiveAppShell`, workspace layouts, auth shell). Prefer adapting the existing shell over a parallel tree.
2. Define named content slots that screens will fill, for example: `header`, `filters`, `body`, `primaryAction`, `footer`, `sidePanel` — only slots visible in the specimens.
3. Wire composed shared components listed above; if a component is missing, implement that component prompt first.
4. Apply breakpoint behavior from `frontend/.cursor/layouts.mdc`:
   - `<600` one column / bottom nav or drawer when the specimens show it
   - `600–1199` rail / compact side nav
   - `≥1200` menu bar + side nav as shown
5. Enforce max content widths appropriate to the layout purpose (auth, form, detail, dashboard, data-heavy).
6. Integrate with `AsyncStateScaffold` so host screens can pass loading/empty/error/forbidden states without custom scaffolds.
7. Localize only chrome owned by the layout; leave screen-specific copy to callers.
8. Add widget + golden tests for all six specimens.
9. Update consuming screens to select this layout by slug from `screen.json` instead of bespoke scaffolding.

## Reusability checklist

- [ ] One layout slug → one shared implementation
- [ ] Screens pass slots/providers; layout does not own feature repositories
- [ ] Works for every surface listed in `layout.json`
- [ ] Navigation destinations omitted when unauthorized (caller + permissions)
- [ ] No hard-coded feature routes inside the layout except optional documented slot defaults

## Backend linkage

Layouts are structural. Backend pairing belongs to each **screen** that uses `{slug}`. Ensure the layout supports the states those screens declare (`loading`, `empty`, `error`, `forbidden`, `offline`, `conflict`) via slots or `AsyncStateScaffold`, so backend-driven states render consistently.

## Done when

- Specimens matched across breakpoints/themes
- At least one real screen composes this layout through shared APIs
- Goldens/tests pass
- `app-ui` screens that declare `layout: "{slug}"` can mount without forking chrome

## Do not

- Duplicate this layout inside a feature folder
- Bake module-specific business logic into the shell
- Ignore tablet/desktop specimens
- Ship without empty/loading regions the specimens show
"""


def write_index(rows: list[dict]) -> None:
    by_module: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        by_module[row["module"]].append(row)

    lines = [
        "# App UI — implementation prompts",
        "",
        "Professional, actionable prompts for every `app-ui` pack that has visual specimens.",
        "Each leaf folder contains `IMPLEMENTATION_PROMPT.md` ready to paste into an agent session.",
        "",
        "Regenerate:",
        "",
        "```bash",
        "python app-ui/tool/generate_implementation_prompts.py",
        "```",
        "",
        "## How to use",
        "",
        "1. Pick the next unfinished screen from `frontend/dev-plan/slices/chronology.yaml` (screens only).",
        "2. Open that folder's `IMPLEMENTATION_PROMPT.md` and paste it into the agent.",
        "3. For missing shared chrome, run the matching **component** or **layout** prompt first.",
        "4. Follow the playbook in `frontend/dev-plan/25-slice-execution-playbook.md`.",
        "",
        f"## Inventory ({len(rows)} prompts)",
        "",
        "| Module | Screens | Components | Layouts |",
        "| --- | ---: | ---: | ---: |",
    ]

    for module in sorted(by_module):
        items = by_module[module]
        screens = sum(1 for i in items if i["kind"] == "screen")
        components = sum(1 for i in items if i["kind"] == "component")
        layouts = sum(1 for i in items if i["kind"] == "layout")
        lines.append(f"| `{module}` | {screens} | {components} | {layouts} |")

    lines.extend(["", "## Prompt index", ""])

    for module in sorted(by_module):
        lines.append(f"### `{module}`")
        lines.append("")
        for item in sorted(by_module[module], key=lambda r: (r["kind"], r["rel"])):
            chrono = f" · `{item['seq']}`" if item.get("seq") else ""
            lines.append(
                f"- **{item['kind']}** [`{item['title']}`]({item['rel']}/{OUT_NAME}){chrono}"
            )
        lines.append("")

    lines.extend(
        [
            "## Rules referenced across prompts",
            "",
            "Root: `.cursor/mandatories.mdc`, `.cursor/app-write-up.mdc`",
            "",
            "Frontend: `frontend/.cursor/index.mdc`, `product_delivery.mdc`, `feature_workflow.mdc`, "
            "`project_structure.mdc`, `components.mdc`, `layouts.mdc`, `ui-workspace.mdc`, "
            "`permissions.mdc`, `network_api.mdc`, `testing.mdc`, and related owners listed in each prompt.",
            "",
            "Backend: `backend/.cursor/vertical-slice-delivery.mdc`, `module-creation.mdc`, `api.mdc`, "
            "`prisma.mdc`, `auth-security.mdc`, plus `backend/dev-plan/P016_slice_pairing.md`.",
            "",
            "Plan: `frontend/dev-plan/00-execution-policy.md`, `25-slice-execution-playbook.md`, "
            "`slices/chronology.yaml`.",
            "",
        ]
    )

    (APP_UI / INDEX_NAME).write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    chronology = load_chronology()
    rows: list[dict] = []
    written = 0

    # Screens: any folder with screen.json (except nested under components/layouts kits only)
    for screen_json in sorted(APP_UI.rglob("screen.json")):
        folder = screen_json.parent
        parts = folder.relative_to(APP_UI).parts
        if not parts:
            continue
        module = parts[0]
        if module.startswith("__"):
            continue
        screen = folder.name
        meta = json.loads(screen_json.read_text(encoding="utf-8"))
        chrono = chronology.get((module, screen))
        text = screen_prompt(folder, module, screen, meta, chrono)
        (folder / OUT_NAME).write_text(text, encoding="utf-8")
        written += 1
        rows.append(
            {
                "kind": "screen",
                "module": module,
                "title": meta.get("title", screen),
                "rel": "/".join(parts).replace("\\", "/"),
                "seq": chrono.get("seq") if chrono else None,
            }
        )

    # Components
    components_root = APP_UI / "00-shared" / "components"
    for component_json in sorted(components_root.rglob("component.json")):
        folder = component_json.parent
        parts = folder.relative_to(APP_UI).parts
        # 00-shared/components/<category>/<slug>
        category = parts[2]
        slug = parts[3]
        meta = json.loads(component_json.read_text(encoding="utf-8"))
        text = component_prompt(folder, category, slug, meta)
        (folder / OUT_NAME).write_text(text, encoding="utf-8")
        written += 1
        rows.append(
            {
                "kind": "component",
                "module": "00-shared",
                "title": f"{category}/{slug}",
                "rel": "/".join(parts).replace("\\", "/"),
                "seq": None,
            }
        )

    # Layouts
    layouts_root = APP_UI / "00-shared" / "layouts"
    for layout_json in sorted(layouts_root.rglob("layout.json")):
        folder = layout_json.parent
        parts = folder.relative_to(APP_UI).parts
        slug = folder.name
        meta = json.loads(layout_json.read_text(encoding="utf-8"))
        text = layout_prompt(folder, slug, meta)
        (folder / OUT_NAME).write_text(text, encoding="utf-8")
        written += 1
        rows.append(
            {
                "kind": "layout",
                "module": "00-shared",
                "title": slug,
                "rel": "/".join(parts).replace("\\", "/"),
                "seq": None,
            }
        )

    write_index(rows)
    print(f"Wrote {written} prompts + {INDEX_NAME}")


if __name__ == "__main__":
    main()
