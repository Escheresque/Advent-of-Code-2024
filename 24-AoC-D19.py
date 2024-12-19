from copy import deepcopy
from collections import defaultdict
from functools import cache
import re

patterns = []
designs = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D19.txt") as file:
    for l, line in enumerate(file):
        if l == 0:
            patterns.extend(list(line.rstrip().split(", ")))
        if l > 1:
            designs.append(line.rstrip())

patternDict = defaultdict(list)
for pat in patterns:
    patternDict[pat[0]].append(pat)

@cache
def check_design(design):
    global patterns
    if not design:
        return 1
    total = 0
    for pat in patterns.get(design[0], []):
        if design.startswith(pat):
            total += check_design(design.removeprefix(pat))
    return total

def part1(designs):
    return sum(check_design(des) > 0 for des in designs)

def part2(designs):
    return sum(check_design(des) for des in designs)

patterns = patternDict
print('P1 Solution: ', part1(designs))
print('P2 Solution: ', part2(designs))

 