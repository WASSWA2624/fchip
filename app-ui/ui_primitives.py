"""Shared visual primitives for FCHIP screen and kit mockups."""

from __future__ import annotations

from PIL import ImageDraw, ImageFont

C = {
    "bg": (247, 250, 249),
    "surface": (255, 255, 255),
    "ink": (26, 46, 53),
    "muted": (90, 110, 118),
    "line": (214, 226, 224),
    "primary": (0, 109, 119),
    "primary_soft": (214, 237, 239),
    "accent": (20, 145, 155),
    "warn": (196, 92, 38),
    "warn_soft": (255, 236, 224),
    "ok": (46, 125, 90),
    "ok_soft": (220, 240, 230),
    "map": (168, 206, 198),
    "map_hot": (196, 92, 38),
    "chrome": (18, 38, 44),
    "white": (255, 255, 255),
    "on_primary": (255, 255, 255),
    "canvas": (236, 242, 240),
}

DARK_C = {
    "bg": (13, 27, 31),
    "surface": (20, 40, 45),
    "ink": (242, 248, 247),
    "muted": (181, 200, 201),
    "line": (53, 81, 88),
    "primary": (88, 197, 204),
    "primary_soft": (23, 60, 66),
    "accent": (115, 213, 219),
    "warn": (255, 181, 143),
    "warn_soft": (74, 41, 30),
    "ok": (126, 214, 172),
    "ok_soft": (23, 59, 44),
    "map": (49, 93, 89),
    "map_hot": (255, 181, 143),
    "chrome": (8, 19, 22),
    "white": (255, 255, 255),
    "on_primary": (8, 19, 22),
    "canvas": (10, 22, 25),
}

SIZES = {
    "mobile": (390, 844),
    "tablet": (768, 1024),
    "desktop": (1440, 900),
}


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def rr(draw: ImageDraw.ImageDraw, box, fill, radius=12, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def tx(draw, xy, value, size=14, bold=False, fill=None, anchor=None):
    draw.text(xy, value, font=font(size, bold), fill=fill or C["ink"], anchor=anchor)


def wrap(draw, value: str, max_w: int, size=13) -> list[str]:
    selected_font = font(size)
    words = value.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if draw.textlength(trial, font=selected_font) <= max_w:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines or [value]
