#!/usr/bin/env python3
# Can be used before any git commit
# Example: ./tools/clean_notebook.py ./notebooks/Untitled.ipynb
import sys, io, os, json

dir_path = os.getcwd()

import os, subprocess

files = sys.argv[1:]

for fname in files:
    print("- Cleaning " + fname + "...")
    with open(fname) as json_data:
        nb = json.load(json_data)

    cells_new = []
    for cell in nb["cells"]:
        if cell["cell_type"] == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
        cell["metadata"] = {}
        cells_new.append(cell)
    nb["cells"] = cells_new
    base, ext = os.path.splitext(fname)
    with open(fname, 'w') as f:
        json.dump(nb, f, indent=2, sort_keys=True)