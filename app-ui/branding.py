"""FCHIP brand assets for app-ui mockups.

Loads logos from `frontend/assets/logos` (source of truth) so kit and screen
specimens stay aligned with the Flutter asset pack.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from PIL import Image

REPO_ROOT = Path(__file__).resolve().parents[1]
LOGOS_DIR = REPO_ROOT / "frontend" / "assets" / "logos"

LOGO_MARK = "logo.png"
LOGO_SPLASH = "splash.png"
LOGO_FAVICON = "favicon.png"

# Product primary teal — used when the mark sits on a light surface.
PRIMARY_TINT = (0, 109, 119)


@lru_cache(maxsize=8)
def load_logo(name: str = LOGO_MARK) -> Image.Image:
    path = LOGOS_DIR / name
    if not path.is_file():
        raise FileNotFoundError(f"Missing brand logo: {path}")
    return Image.open(path).convert("RGBA")


def tinted_logo(name: str = LOGO_MARK, color: tuple[int, int, int] = PRIMARY_TINT) -> Image.Image:
    """Recolor opaque logo pixels while keeping the alpha mask."""
    src = load_logo(name)
    alpha = src.split()[3]
    solid = Image.new("RGBA", src.size, (*color, 255))
    solid.putalpha(alpha)
    return solid


def fit_logo(
    name: str,
    max_w: int,
    max_h: int,
    *,
    tint: tuple[int, int, int] | None = PRIMARY_TINT,
) -> Image.Image:
    img = tinted_logo(name, tint) if tint else load_logo(name).copy()
    img.thumbnail((max_w, max_h), Image.Resampling.LANCZOS)
    return img


def paste_logo(
    canvas: Image.Image,
    xy: tuple[int, int] | tuple[float, float],
    *,
    name: str = LOGO_MARK,
    max_w: int = 160,
    max_h: int = 160,
    tint: tuple[int, int, int] | None = PRIMARY_TINT,
    anchor: str = "lt",
) -> tuple[int, int]:
    """Paste a fitted logo onto `canvas`. Returns pasted size (w, h).

    Pass ``tint=None`` to keep the asset colors (white mark for dark chrome).
    """
    logo = fit_logo(name, max_w, max_h, tint=tint)
    lw, lh = logo.size
    x, y = float(xy[0]), float(xy[1])
    h_anchor = anchor[0] if anchor else "l"
    v_anchor = anchor[1] if len(anchor) > 1 else "t"
    if h_anchor == "m":
        x -= lw / 2
    elif h_anchor == "r":
        x -= lw
    if v_anchor == "m":
        y -= lh / 2
    elif v_anchor == "b":
        y -= lh
    if canvas.mode != "RGBA":
        overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        overlay.paste(logo, (int(x), int(y)), logo)
        composed = Image.alpha_composite(canvas.convert("RGBA"), overlay)
        canvas.paste(composed.convert(canvas.mode))
    else:
        canvas.paste(logo, (int(x), int(y)), logo)
    return lw, lh


def paste_logo_centered(
    canvas: Image.Image,
    cx: float,
    cy: float,
    *,
    name: str = LOGO_MARK,
    max_w: int = 160,
    max_h: int = 160,
    tint: tuple[int, int, int] | None = PRIMARY_TINT,
) -> tuple[int, int]:
    return paste_logo(
        canvas,
        (cx, cy),
        name=name,
        max_w=max_w,
        max_h=max_h,
        tint=tint,
        anchor="mm",
    )
