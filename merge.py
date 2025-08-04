#!/bin/env python3

import sys
import json
from collections.abc import Mapping

def deep_merge(a, b):
    """Recursively merge dict b into dict a."""
    for key in b:
        if key in a and isinstance(a[key], dict) and isinstance(b[key], dict):
            deep_merge(a[key], b[key])
        else:
            a[key] = b[key]
    return a

def load_json(path):
    with open(path, 'r') as f:
        return json.load(f)

def main(file1, file2):
    data1 = load_json(file1)
    data2 = load_json(file2)

    if not isinstance(data1, Mapping) or not isinstance(data2, Mapping):
        print("Top-level JSON values must be objects", file=sys.stderr)
        sys.exit(1)

    merged = deep_merge(data1, data2)
    json.dump(merged, sys.stdout, indent=2)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python merge_json.py file1.json file2.json", file=sys.stderr)
        sys.exit(1)
    main(sys.argv[1], sys.argv[2])
