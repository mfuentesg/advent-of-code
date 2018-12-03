#!/bin/python3

import sys
import itertools

frequencies = {0}
r = 0
lines = [int(x) for x in sys.stdin.readlines()]
for n in itertools.cycle(lines):
    r += n
    if r in frequencies:
        break
    frequencies.add(r)
print(r)
