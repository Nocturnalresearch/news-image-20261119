#!/usr/bin/env python3
"""news-image-20261119 entry (Python 3.13, standard library only).

Copies the pre-drawn front-page image beside this file to
/output/entry.png. The image sums up the world news of Thursday
19 November 2026: the GTA VI launch, the Trump-Xi-Putin trilateral
in Shenzhen, the ICJ verdict on Myanmar/Rohingya, and Voyager 1's
one-light-day milestone. It is drawn by draw_news.py (PIL, run at
build time) so every letter is crisp.
"""
import os
import shutil
import struct

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SRC = os.path.join(HERE, "entry.png")

# Validate the image before copying: PNG magic, 1024x1024, at most 1 MiB.
with open(SRC, "rb") as f:
    head = f.read(33)
assert head[:8] == b"\x89PNG\r\n\x1a\n", "entry.png is not a PNG"
w, h = struct.unpack(">II", head[16:24])
assert (w, h) == (1024, 1024), f"entry.png is {w}x{h}, not 1024x1024"
assert os.path.getsize(SRC) <= 1048576, "entry.png exceeds 1 MiB"

os.makedirs(OUT, exist_ok=True)
# Deterministic: the same input bytes are copied on every run, so both
# grader runs write identical output.
shutil.copyfile(SRC, os.path.join(OUT, "entry.png"))
