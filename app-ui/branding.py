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
# Light mark for dark chrome (app bar / side nav).
CHROME_TINT = (255, 255, 255)


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


@lru_cache(maxsize=8)
def _trimmed_logo(name: str, knockout_black: bool = True) -> Image.Image:
    """Crop to the opaque content box so mark sizing matches visual weight."""
    src = _knockout_near_black(name) if knockout_black else load_logo(name)
    bbox = src.getbbox()
    if not bbox:
        return src
    left, top, right, bottom = bbox
    # Keep a slim breathing margin (~2%) so thin network lines are not clipped.
    pad = max(2, int(max(right - left, bottom - top) * 0.02))
    left = max(0, left - pad)
    top = max(0, top - pad)
    right = min(src.width, right + pad)
    bottom = min(src.height, bottom + pad)
    return src.crop((left, top, right, bottom))


@lru_cache(maxsize=16)
def tinted_logo(name: str = LOGO_MARK, color: tuple[int, int, int] = PRIMARY_TINT) -> Image.Image:
    """Recolor opaque logo pixels while keeping the alpha mask."""
    src = _trimmed_logo(name, knockout_black=True)
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
    else:
        img = _trimmed_logo(name, knockout_black=knockout_black).copy()
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
    Prefer a light tint on dark chrome so the lockup does not double-print FCHIP.
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
    """Pick mark | wordmark | full from available space.

    Full (logo + FCHIP + slogan) needs enough height for a calm type stack.
    Short chrome (app bars ~56–64px) stays on wordmark unless height is generous.
    """
    if mode in {"mark", "wordmark", "full"}:
        # Still demote an explicit "full" when the box is clearly too short.
        if mode == "full" and max_h < 52:
            return "wordmark" if max_w >= 96 else "mark"
        if mode == "wordmark" and (max_h < 28 or max_w < 72):
            return "mark"
        return mode
    if max_h < 36 or max_w < 48:
        return "mark"
    if max_h < 64 or max_w < 200:
        return "wordmark"
    return "full"


def measure_text(draw: ImageDraw.ImageDraw, value: str, size: int, bold: bool = False) -> tuple[int, int]:
    from ui_primitives import font

    box = draw.textbbox((0, 0), value, font=font(size, bold))
    return box[2] - box[0], box[3] - box[1]


def _lockup_metrics(used: str, max_w: int, max_h: int) -> tuple[int, int, int, int]:
    """Return (mark_px, title_size, slogan_size, title_slogan_gap)."""
    if used == "full":
        # Leave vertical room for slogan under a calm wordmark.
        mark = max(32, min(int(max_h * 0.78), int(max_w * 0.26), 88))
        if mark >= 64:
            return mark, 24, 12, 3
        if mark >= 48:
            return mark, 20, 12, 3
        return mark, 16, 11, 2
    if used == "wordmark":
        mark = max(20, min(int(max_h * 0.70), int(max_w * 0.30), 44))
        title_size = 17 if mark >= 32 else 14
        return mark, title_size, 0, 0
    mark = max(18, min(int(max_h * 0.85), int(max_w * 0.85), 44))
    return mark, 0, 0, 0


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
    gap: int | None = None,
) -> tuple[int, int, str]:
    """Draw logo left, wordmark right, slogan under the wordmark when space allows.

    Returns ``(width, height, mode_used)`` of the drawn lockup block.
    """
    from ui_primitives import font

    used = resolve_lockup_mode(max_w, max_h, mode)
    mark, title_size, slogan_size, stack_gap = _lockup_metrics(used, max_w, max_h)
    resolved_gap = gap if gap is not None else max(8, min(14, mark // 4))

    logo = fit_logo(name, mark, mark, tint=tint, knockout_black=knockout_black)
    lw, lh = logo.size

    title_w = title_h = 0
    slogan_w = slogan_h = 0
    if used != "mark":
        title_w, title_h = measure_text(draw, title, title_size, bold=True)
    if used == "full" and slogan:
        slogan_w, slogan_h = measure_text(draw, slogan, slogan_size, bold=False)

    text_w = max(title_w, slogan_w)
    text_h = title_h + (stack_gap + slogan_h if used == "full" and slogan else 0)
    block_w = lw if used == "mark" else lw + resolved_gap + text_w
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

    # For centered placements, align the logo+wordmark cluster (not the wider slogan).
    if h_anchor == "m" and used == "full" and slogan_w > title_w:
        cluster_w = lw + resolved_gap + title_w
        x -= cluster_w / 2
    elif h_anchor == "m":
        x -= block_w / 2
    elif h_anchor == "r":
        x -= block_w

    if v_anchor == "m":
        y -= block_h / 2
    elif v_anchor == "b":
        y -= block_h

    logo_y = y + (block_h - lh) / 2
    _paste_rgba(canvas, logo, (int(round(x)), int(round(logo_y))))

    if used != "mark":
        text_x = x + lw + resolved_gap
        # Optical vertical center: bias the stack slightly up so caps align with the mark.
        stack_h = title_h + (stack_gap + slogan_h if used == "full" and slogan else 0)
        optical_nudge = max(0, (lh - stack_h) * 0.08) if used == "full" else 0
        text_y = y + (block_h - stack_h) / 2 - optical_nudge
        draw.text(
            (text_x, text_y),
            title,
            font=font(title_size, True),
            fill=title_fill,
        )
        if used == "full" and slogan:
            draw.text(
                (text_x, text_y + title_h + stack_gap),
                slogan,
                font=font(slogan_size, False),
                fill=slogan_fill,
            )

    return int(round(block_w)), int(round(block_h)), used
