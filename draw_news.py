#!/usr/bin/env python3
"""Draw the 19 November 2026 world-news front page (1024x1024 PNG).

One image summing up the day's news, drawn entirely with PIL so every
letter is crisp and legible (no AI-garbled text). Layout: masthead with
the date, then a 2x2 grid of stories, each with a small illustration,
a region tag, a bold headline and a one-line subhead.

Stories (researched from Reuters/AP/AFP/WSJ and NASA coverage of 19 Nov 2026):
  1. GTA VI launches TODAY — 13 years after GTA V, PS5 & Xbox, Metacritic 99.
  2. Trump-Xi-Putin trilateral in Shenzhen — first-ever three-way summit,
     nuclear arms and the Iran war on the table.
  3. ICJ rules on Myanmar/Rohingya genocide — verdict delivered today in
     The Hague, seven-year case, first state verdict if guilty.
  4. Voyager 1 one light-day out — NASA marks the milestone today; a radio
     signal now takes a full day to reach the probe.
"""
import math
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (250, 247, 240)
NAVY = (15, 42, 74)
NAVY_DARK = (10, 26, 46)
GOLD = (232, 193, 90)
INK = (20, 28, 38)
GRAY = (68, 68, 68)
WHITE = (255, 255, 255)

F_SERIF_B = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
F_SANS_B = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def vgrad(img, box, top, bottom):
    """Vertical gradient inside box (x0, y0, x1, y1)."""
    x0, y0, x1, y1 = box
    h = max(1, y1 - y0)
    for y in range(h):
        t = y / h
        c = tuple(int(top[i] + (bottom[i] - top[i]) * t) for i in range(3))
        img.paste(c, (x0, y0 + y, x1, y0 + y + 1))


def wrap(draw, text, fnt, max_w):
    """Wrap text to fit max_w pixels; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def centered(draw, text, fnt, y, color, cx=W // 2):
    draw.text((cx, y), text, font=fnt, fill=color, anchor="mt")


def starburst(d, cx, cy, r_out, r_in, n=12, color=(255, 140, 0)):
    pts = []
    for i in range(n * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.pi * i / n
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=color)


def draw_gta_launch(d, box):
    """Vice City sunset: pink-orange sky, sun, skyline, palms, big VI."""
    x0, y0, x1, y1 = box
    vgrad(d._image, box, (194, 24, 91), (255, 152, 0))
    # sun
    d.ellipse([x0 + 196, y0 + 22, x0 + 292, y0 + 118], fill=(255, 236, 160))
    # skyline silhouettes
    base = y1
    heights = [66, 104, 78, 122, 88, 108, 70, 96]
    bw = (x1 - x0) // len(heights)
    for i, hh in enumerate(heights):
        d.rectangle([x0 + i * bw + 3, base - hh, x0 + (i + 1) * bw - 3, base],
                    fill=(30, 8, 40))
    # palm trees: one on each side, kept inside the box; fronds droop
    # downward in two segments so they read as palms, not a "T"
    for px, ph in [(66, 92), (420, 80)]:
        top_x, top_y = x0 + px + 10, base - ph
        d.line([x0 + px, base, top_x, top_y], fill=(20, 6, 28), width=7)
        for ang in (-75, -45, -15, 15, 45, 75):
            r = math.radians(ang)
            mid_x = top_x + 20 * math.sin(r)
            mid_y = top_y - 6 + 14 * math.cos(r) * 0.4
            end_x = top_x + 38 * math.sin(r)
            end_y = top_y + 14 + 6 * math.cos(r) * 0.4
            d.line([top_x, top_y, mid_x, mid_y, end_x, end_y],
                   fill=(20, 6, 28), width=5)
    # big VI over the sun
    f_vi = font(F_SANS_B, 84)
    d.text((x0 + 244, y0 + 6), "VI", font=f_vi, fill=(255, 255, 255), anchor="mt",
           stroke_width=3, stroke_fill=(120, 10, 60))
    # "OUT TODAY" ribbon at the bottom of the illustration
    d.rectangle([x0, y1 - 34, x1, y1], fill=(15, 42, 74))
    f_rib = font(F_SANS_B, 22)
    d.text((x0 + (x1 - x0) // 2, y1 - 17), "OUT TODAY", font=f_rib,
           fill=(232, 193, 90), anchor="mm")


def draw_summit(d, box):
    """Three flags (China, Russia, USA) above a Shenzhen skyline."""
    x0, y0, x1, y1 = box
    vgrad(d._image, box, (240, 234, 222), (214, 204, 186))
    # skyline silhouettes
    base = y1
    heights = [58, 92, 70, 110, 78, 96, 62, 88]
    bw = (x1 - x0) // len(heights)
    for i, hh in enumerate(heights):
        d.rectangle([x0 + i * bw + 4, base - hh, x0 + (i + 1) * bw - 4, base],
                    fill=(52, 58, 66))
    # three flags on poles above the skyline
    flag_w, flag_h = 96, 64
    fy = y0 + 14
    # China: red field, one gold star
    fx = x0 + 62
    d.rectangle([fx, fy, fx + flag_w, fy + flag_h], fill=(222, 41, 16))
    starburst(d, fx + 22, fy + 20, 12, 5, n=5, color=(255, 222, 0))
    # Russia: white / blue / red horizontal stripes
    fx = x0 + 196
    d.rectangle([fx, fy, fx + flag_w, fy + 22], fill=(255, 255, 255))
    d.rectangle([fx, fy + 22, fx + flag_w, fy + 43], fill=(0, 57, 166))
    d.rectangle([fx, fy + 43, fx + flag_w, fy + flag_h], fill=(213, 0, 50))
    d.rectangle([fx, fy, fx + flag_w, fy + flag_h], outline=(120, 120, 120), width=2)
    # USA: red/white stripes + blue canton
    fx = x0 + 330
    for s in range(7):
        d.rectangle([fx, fy + s * 9, fx + flag_w, fy + s * 9 + 9],
                    fill=(178, 34, 52) if s % 2 == 0 else (255, 255, 255))
    d.rectangle([fx, fy, fx + 40, fy + 34], fill=(60, 59, 110))
    d.rectangle([fx, fy, fx + flag_w, fy + flag_h], outline=(120, 120, 120), width=2)


def draw_icj(d, box):
    """The Hague courthouse: pediment, columns, scales of justice."""
    x0, y0, x1, y1 = box
    vgrad(d._image, box, (188, 214, 232), (226, 234, 240))
    # pediment (triangle) on top of the courthouse
    cx = (x0 + x1) // 2
    d.polygon([(x0 + 60, y0 + 58), (x1 - 60, y0 + 58), (cx, y0 + 12)], fill=(70, 78, 88))
    d.rectangle([x0 + 60, y0 + 58, x1 - 60, y0 + 70], fill=(52, 58, 66))
    # columns
    for col_x in (96, 186, 276, 366):
        d.rectangle([x0 + col_x, y0 + 70, x0 + col_x + 26, y1 - 18], fill=(240, 238, 230))
        d.rectangle([x0 + col_x - 4, y0 + 70, x0 + col_x + 30, y0 + 78], fill=(220, 218, 210))
        d.rectangle([x0 + col_x - 4, y1 - 26, x0 + col_x + 30, y1 - 18], fill=(220, 218, 210))
    # base steps
    d.rectangle([x0 + 40, y1 - 18, x1 - 40, y1 - 10], fill=(90, 96, 104))
    d.rectangle([x0 + 24, y1 - 10, x1 - 24, y1 - 2], fill=(70, 76, 84))
    # scales of justice, centred on the pediment
    sx, sy = cx, y0 + 34
    d.line([sx, sy - 6, sx, sy + 14], fill=(232, 193, 90), width=3)
    d.line([sx - 26, sy - 2, sx + 26, sy - 2], fill=(232, 193, 90), width=3)
    d.arc([sx - 34, sy - 2, sx - 14, sy + 14], start=0, end=180, fill=(232, 193, 90), width=3)
    d.arc([sx + 14, sy - 2, sx + 34, sy + 14], start=0, end=180, fill=(232, 193, 90), width=3)
    d.line([sx - 26, sy - 2, sx - 24, sy + 8], fill=(232, 193, 90), width=2)
    d.line([sx + 26, sy - 2, sx + 24, sy + 8], fill=(232, 193, 90), width=2)


def draw_voyager(d, box):
    """Deep space: black sky, stars, Voyager probe with dish and signal rings."""
    x0, y0, x1, y1 = box
    vgrad(d._image, box, (4, 8, 20), (16, 28, 58))
    # stars
    import random
    rng = random.Random(1911)
    for _ in range(70):
        sx = rng.randint(x0 + 6, x1 - 6)
        sy = rng.randint(y0 + 6, y1 - 6)
        r = rng.choice([1, 1, 2])
        d.ellipse([sx - r, sy - r, sx + r, sy + r], fill=(255, 255, 255))
    # a few bright stars with cross sparkle
    for sx, sy in [(x0 + 70, y0 + 30), (x0 + 400, y0 + 52), (x0 + 120, y0 + 140)]:
        d.line([sx - 8, sy, sx + 8, sy], fill=(255, 255, 255), width=2)
        d.line([sx, sy - 8, sx, sy + 8], fill=(255, 255, 255), width=2)
    # signal rings expanding from the probe toward Earth (lower-left)
    px, py = x0 + 300, y0 + 92
    for r, w in [(44, 2), (72, 2), (100, 2)]:
        d.arc([px - r, py - r, px + r, py + r], start=120, end=300,
              fill=(120, 190, 255), width=w)
    # probe body
    d.rectangle([px - 8, py - 26, px + 8, py + 26], fill=(200, 205, 215))
    d.rectangle([px - 22, py - 10, px + 22, py + 10], fill=(160, 165, 178))
    # high-gain dish (white circle) facing lower-left
    d.ellipse([px - 78, py + 6, px - 18, py + 66], fill=(235, 238, 245))
    d.ellipse([px - 66, py + 18, px - 30, py + 54], fill=(180, 185, 198))
    d.line([px - 22, py + 30, px - 8, py + 18], fill=(200, 205, 215), width=4)
    # boom with magnetometer
    d.line([px + 8, py - 10, px + 66, py - 44], fill=(200, 205, 215), width=4)
    d.rectangle([px + 62, py - 50, px + 74, py - 38], fill=(232, 193, 90))
    # RTG boom (lower-right)
    d.line([px + 6, py + 16, px + 52, py + 52], fill=(200, 205, 215), width=4)
    d.rectangle([px + 48, py + 48, px + 62, py + 62], fill=(232, 193, 90))
    # Earth as a small blue dot, lower-left, with the signal reaching it
    ex, ey = x0 + 52, y1 - 30
    d.ellipse([ex - 12, ey - 12, ex + 12, ey + 12], fill=(70, 130, 220))
    d.ellipse([ex - 7, ey - 8, ex + 3, ey + 2], fill=(120, 190, 120))


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- masthead ----
    d.rectangle([0, 0, W, 128], fill=NAVY)
    d.rectangle([0, 128, W, 132], fill=GOLD)
    centered(d, "WORLD NEWS", font(F_SERIF_B, 62), 12, WHITE)
    centered(d, "THURSDAY, 19 NOVEMBER 2026", font(F_SANS_B, 30), 84, GOLD)

    # ---- tagline ----
    centered(d, "Four stories that defined the day", font(F_SANS, 21), 140, GRAY)

    # ---- panels ----
    stories = [
        ("CULTURE", (123, 31, 162), draw_gta_launch,
         "GTA VI launches today, 13 years after GTA V",
         "Metacritic 99; PS5 and Xbox unlock at midnight"),
        ("CHINA", (176, 32, 32), draw_summit,
         "Trump, Xi and Putin meet in Shenzhen",
         "First three-way summit; nuclear arms and Iran on the table"),
        ("THE HAGUE", (0, 90, 160), draw_icj,
         "World Court rules on Rohingya genocide",
         "Seven-year case; a first state verdict if Myanmar is guilty"),
        ("SPACE", (10, 26, 46), draw_voyager,
         "Voyager 1, one light-day from Earth",
         "NASA marks the milestone; a signal now takes a full day"),
    ]
    margin, gap = 16, 16
    pw = (W - margin * 2 - gap) // 2
    ph = (958 - 166 - gap) // 2
    f_tag = font(F_SANS_B, 16)
    f_head = font(F_SANS_B, 30)
    f_sub = font(F_SANS, 19)
    for i, (tag, color, artist, head, sub) in enumerate(stories):
        px = margin + (i % 2) * (pw + gap)
        py = 166 + (i // 2) * (ph + gap)
        # card background + border
        d.rectangle([px, py, px + pw, py + ph], fill=WHITE, outline=(200, 196, 188), width=2)
        # illustration
        artist(d, (px + 2, py + 2, px + pw - 2, py + 182))
        # tag strip
        d.rectangle([px + 2, py + 182, px + pw - 2, py + 212], fill=color)
        d.text((px + 14, py + 197), tag, font=f_tag, fill=WHITE, anchor="lm")
        # headline (2 lines)
        lines = wrap(d, head, f_head, pw - 28)
        y = py + 224
        for ln in lines[:2]:
            d.text((px + 14, y), ln, font=f_head, fill=INK)
            y += 36
        # subhead (2 lines)
        lines = wrap(d, sub, f_sub, pw - 28)
        y = py + 224 + 36 * min(2, len(wrap(d, head, f_head, pw - 28))) + 6
        for ln in lines[:2]:
            d.text((px + 14, y), ln, font=f_sub, fill=GRAY)
            y += 24

    # ---- footer ----
    d.rectangle([0, 966, W, H], fill=NAVY_DARK)
    centered(d, "Sources: Reuters  ·  AP  ·  AFP  ·  NASA     —     19 November 2026",
             font(F_SANS, 16), 984, (200, 205, 215))

    img.save("entry.png", "PNG", optimize=True)
    print("saved entry.png", img.size)


if __name__ == "__main__":
    main()
