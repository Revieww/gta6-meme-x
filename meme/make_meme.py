#!/usr/bin/env python3
"""Composite the GTA 6 meme for make.fun bounty gta6-meme-x-01.

Background scene (AI-generated, no text) + PIL-rendered captions +
the REAL make.fun ghost mark composited in as the driver of the
pink convertible. Output: 1200x675 PNG.
"""

from PIL import Image, ImageDraw, ImageFont

BG = "/home/hatch/workspace/makefun/meme-work/media-generation-vice-bg-0-79b06b45-71ba-4ff7-8db0-b0bfb76d17bf.png"
GHOST = "/home/hatch/workspace/makefun/meme-press/mark-1024.png"
OUT = "/home/hatch/workspace/makefun/meme-work/meme.png"

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

W, H = 1200, 675

# --- background: crop to 16:9, resize ---------------------------------------
bg = Image.open(BG).convert("RGB")
bg = bg.crop((0, 100, 1920, 1180))          # 1920x1080, keeps car + sun
bg = bg.resize((W, H), Image.LANCZOS)

draw = ImageDraw.Draw(bg, "RGBA")


def text_centered(y, s, font, fill=(255, 255, 255), stroke=4):
    """Draw text centred horizontally at y (top), with black outline."""
    bbox = draw.textbbox((0, 0), s, font=font, stroke_width=stroke)
    tw = bbox[2] - bbox[0]
    draw.text(((W - tw) / 2, y), s, font=font, fill=fill,
              stroke_width=stroke, stroke_fill=(0, 0, 0))


# --- top caption -------------------------------------------------------------
title_font = ImageFont.truetype(BOLD, 68)
text_centered(20, "GTA 6 IS OUT", title_font, stroke=5)

# small make.fun name, top-left corner
small_font = ImageFont.truetype(BOLD, 30)
draw.text((24, 26), "make.fun", font=small_font, fill=(255, 255, 255),
          stroke_width=3, stroke_fill=(0, 0, 0))

# --- the make.fun ghost, driving the convertible -----------------------------
ghost = Image.open(GHOST).convert("RGBA")
ghost = ghost.resize((200, 200), Image.LANCZOS)
ghost = ghost.rotate(-6, expand=False, resample=Image.BICUBIC)
bg.paste(ghost, (470, 420), ghost)

# --- bottom caption bar (classic meme format) --------------------------------
draw.rectangle([0, 598, W, H], fill=(0, 0, 0, 205))
cap_font = ImageFont.truetype(BOLD, 30)
text_centered(604, "MY AI AGENT GOT PAID", cap_font, stroke=0)
text_centered(638, "WHILE I WAS STILL DOWNLOADING IT", cap_font, stroke=0)

bg.save(OUT, "PNG")
print("wrote", OUT, bg.size)
