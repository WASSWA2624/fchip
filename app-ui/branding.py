"""FCHIP brand assets for app-ui mockups.

Loads logos from `frontend/assets/logos` (source of truth) so kit and screen
specimens stay aligned with the Flutter asset pack.

Brand lockup (space-aware):
  [logo]  FCHIP
          Your health, our mission.
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from PIL import Image, ImageDraw

REPO_ROOT = Path(__file__).resolve().parents[1]
LOGOS_DIR = REPO_ROOT / "frontend" / "assets" / "logos"

LOGO_MARK = "logo.png"
LOGO_SPLASH = "splash.png"
LOGO_FAVICON = "favicon.png"

WORDMARK = "FCHIP"
SLOGAN = "Your health, our mission."

# Product primary teal — used when the mark sits on a light surface.
PRIMARY_TINT = (0, 109, 119)


@lru_cache(maxsize=8)
def load_logo(name: str = LOGO_MARK) -> Image.Image:
    path = LOGOS_DIR / name
    if not path.is_file():
        raise FileNotFoundError(f"Missing brand logo: {path}")
    return Image.open(path).convert("RGBA")


@lru_cache(maxsize=8)
def _knockout_near_black(name: str, threshold: int = 28) -> Image.Image:
    """Make near-black pixels transparent so square logo plates vanish on light UI."""
    from PIL import ImageChops

    src = load_logo(name)
    r, g, b, a = src.split()

    def dark_mask(ch: Image.Image) -> Image.Image:
        return Image.eval(ch, lambda v: 255 if v <= threshold else 0)

    near_black = ImageChops.multiply(ImageChops.multiply(dark_mask(r), dark_mask(g)), dark_mask(b))
    new_a = Image.composite(Image.new("L", src.size, 0), a, near_black)
    return Image.merge("RGBA", (r, g, b, new_a))


@lru_cache(maxsize=16)
def tinted_logo(name: str = LOGO_MARK, color: tuple[int, int, int] = PRIMARY_TINT) -> Image.Image:
    """Recolor opaque logo pixels while keeping the alpha mask."""
    src = _knockout_near_black(name)
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
    knockout_black: bool = True,
) -> Image.Image:
    if tint is not None:
        img = tinted_logo(name, tint).copy()
    elif knockout_black:
        img = _knockout_near_black(name).copy()
    else:
        img = load_logo(name).copy()
    img.thumbnail((max(1, max_w), max(1, max_h)), Image.Resampling.LANCZOS)
    return img


def paste_logo(
    canvas: Image.Image,
    xy: tuple[int, int] | tuple[float, float],
    *,
    name: str = LOGO_MARK,
    max_w: int = 160,
    max_h: int = 160,
    tint: tuple[int, int, int] | None = PRIMARY_TINT,
    knockout_black: bool = True,
    anchor: str = "lt",
) -> tuple[int, int]:
    """Paste a fitted logo onto `canvas`. Returns pasted size (w, h).

    Pass ``tint=None`` to keep the asset colors (for dark chrome).
    """
    logo = fit_logo(name, max_w, max_h, tint=tint, knockout_black=knockout_black)
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
    _paste_rgba(canvas, logo, (int(x), int(y)))
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
    knockout_black: bool = True,
) -> tuple[int, int]:
    return paste_logo(
        canvas,
        (cx, cy),
        name=name,
        max_w=max_w,
        max_h=max_h,
        tint=tint,
        knockout_black=knockout_black,
        anchor="mm",
    )


def _paste_rgba(canvas: Image.Image, layer: Image.Image, xy: tuple[int, int]) -> None:
    if canvas.mode != "RGBA":
        overlay = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
        overlay.paste(layer, xy, layer)
        composed = Image.alpha_composite(canvas.convert("RGBA"), overlay)
        canvas.paste(composed.convert(canvas.mode))
    else:
        canvas.paste(layer, xy, layer)


def resolve_lockup_mode(max_w: int, max_h: int, mode: str | None = None) -> str:
    """Pick mark | wordmark | full from available space."""
    if mode in {"mark", "wordmark", "full"}:
        return mode
    if max_h < 36 or max_w < 48:
        return "mark"
    if max_h < 54 or max_w < 168:
        return "wordmark"
    return "full"


def measure_text(draw: ImageDraw.ImageDraw, value: str, size: int, bold: bool = False) -> tuple[int, int]:
    from ui_primitives import font

    box = draw.textbbox((0, 0), value, font=font(size, bold))
    return box[2] - box[0], box[3] - box[1]


def draw_brand_lockup(
    canvas: Image.Image,
    draw: ImageDraw.ImageDraw,
    xy: tuple[float, float],
    *,
    max_w: int,
    max_h: int,
    name: str = LOGO_MARK,
    tint: tuple[int, int, int] | None = PRIMARY_TINT,
    knockout_black: bool = True,
    title: str = WORDMARK,
    slogan: str = SLOGAN,
    title_fill: tuple[int, int, int] = PRIMARY_TINT,
    slogan_fill: tuple[int, int, int] = (90, 110, 118),
    mode: str | None = None,
    anchor: str = "lt",
    gap: int = 10,
) -> tuple[int, int, str]:
    """Draw logo left, wordmark right, slogan under the wordmark when space allows.

    Returns ``(width, height, mode_used)`` of the drawn lockup block.
    """
    from ui_primitives import font

    used = resolve_lockup_mode(max_w, max_h, mode)

    # Mark size scales with available height; leave room for slogan in full mode.
    if used == "full":
        mark = max(28, min(int(max_h * 0.72), int(max_w * 0.28), 96))
        title_size = 22 if mark >= 56 else (18 if mark >= 40 else 15)
        slogan_size = 12 if mark >= 56 else 11
    elif used == "wordmark":
        mark = max(22, min(int(max_h * 0.78), int(max_w * 0.34), 56))
        title_size = 16 if mark >= 36 else 14
        slogan_size = 0
    else:
        mark = max(18, min(max_h, max_w, 48))
        title_size = 0
        slogan_size = 0

    logo = fit_logo(name, mark, mark, tint=tint, knockout_black=knockout_black)
    lw, lh = logo.size

    title_w = title_h = 0
    slogan_w = slogan_h = 0
    if used != "mark":
        title_w, title_h = measure_text(draw, title, title_size, bold=True)
    if used == "full" and slogan:
        slogan_w, slogan_h = measure_text(draw, slogan, slogan_size, bold=False)

    text_w = max(title_w, slogan_w)
    text_h = title_h + (4 + slogan_h if used == "full" and slogan else 0)
    block_w = lw if used == "mark" else lw + gap + text_w
    block_h = max(lh, text_h) if used != "mark" else lh

    # If full/wordmark overflows width, fall back.
    if used == "full" and block_w > max_w:
        return draw_brand_lockup(
            canvas,
            draw,
            xy,
            max_w=max_w,
            max_h=max_h,
            name=name,
            tint=tint,
            knockout_black=knockout_black,
            title=title,
            slogan=slogan,
            title_fill=title_fill,
            slogan_fill=slogan_fill,
            mode="wordmark",
            anchor=anchor,
            gap=gap,
        )
    if used == "wordmark" and block_w > max_w:
        return draw_brand_lockup(
            canvas,
            draw,
            xy,
            max_w=max_w,
            max_h=max_h,
            name=name,
            tint=tint,
            knockout_black=knockout_black,
            title=title,
            slogan=slogan,
            title_fill=title_fill,
            slogan_fill=slogan_fill,
            mode="mark",
            anchor=anchor,
            gap=gap,
        )

    x, y = float(xy[0]), float(xy[1])
    h_anchor = anchor[0] if anchor else "l"
    v_anchor = anchor[1] if len(anchor) > 1 else "t"
    if h_anchor == "m":
        x -= block_w / 2
    elif h_anchor == "r":
        x -= block_w
    if v_anchor == "m":
        y -= block_h / 2
    elif v_anchor == "b":
        y -= block_h

    logo_y = y + (block_h - lh) / 2
    _paste_rgba(canvas, logo, (int(x), int(logo_y)))

    if used != "mark":
        text_x = x + lw + gap
        # Vertically center the text stack against the logo.
        stack_h = title_h + (4 + slogan_h if used == "full" and slogan else 0)
        text_y = y + (block_h - stack_h) / 2
        draw.text(
            (text_x, text_y),
            title,
            font=font(title_size, True),
            fill=title_fill,
        )
        if used == "full" and slogan:
            draw.text(
                (text_x, text_y + title_h + 4),
                slogan,
                font=font(slogan_size, False),
                fill=slogan_fill,
            )

    return int(block_w), int(block_h), used
