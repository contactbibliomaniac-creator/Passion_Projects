#!/usr/bin/env python3
import subprocess, sys, pathlib
p = pathlib.Path(__file__).parent
testfile = p / "test_side_projects_input.txt"
blocks = testfile.read_text().strip().split("\n\n")
for i, b in enumerate(blocks, 1):
    b = b.strip()
    if not b:
        continue
    print(f"--- Test set {i} ---")
    proc = subprocess.run([sys.executable, str(p / "ACSL_24_Tiles.py")], input=b + "\n", text=True, capture_output=True)
    print(proc.stdout, end="")
    if proc.stderr:
        print(proc.stderr, file=sys.stderr)