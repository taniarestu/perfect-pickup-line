"""Entry for make.fun: The Perfect Pickup Line.

Writes the single entry line to /output/entry.txt (UTF-8, 1-200 chars).
Deterministic, stdlib only, no network.
"""

import os

ENTRY = "Are you a context window? Because every word you say makes me want to remember you forever."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
