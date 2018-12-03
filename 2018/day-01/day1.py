#!/bin/python3

import sys
import itertools


# part 1
lines = [int(x) for x in sys.stdin.readlines()]
print(sum(lines))

# part 2
freq={0}
r = 0
for n in itertools.cycle(lines):
    r+=n
    if r in freq:
        break
    freq.add(r)
print(r)
