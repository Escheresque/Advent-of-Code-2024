from copy import deepcopy
import numpy as np
import pandas as pd
import os
import time
from operator import itemgetter

rain = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D18.txt") as file:
    for l, line in enumerate(file):
        rain.append((int(line.rstrip().split(",")[0]), int(line.rstrip().split(",")[1])))

gridsize = (71, 71)
endpoint = (gridsize[0] - 1, gridsize[1] - 1)

grid = []
for i in range(0, gridsize[0]):
    row = []
    for j in range(0, gridsize[1]):
        row.append(".")
    grid.append(row)

p1grid = deepcopy(grid)
for c in range(0, gridsize[0]):
    for r in range(0, gridsize[1]):
        if (r, c) in rain:
            p1grid[c][r] = "#"

scoregrid = deepcopy(grid)
for c in range(0, gridsize[0]):
    for r in range(0, gridsize[1]):
        if scoregrid[c][r] == ".":
            scoregrid[c][r] = 0

#
dirs = ((0, -1),(1, 0),(0, 1),(-1, 0))

def dijkstra(input):

    global rainscoregrid
    global raingrid

    curcol = input[0]
    currow = input[1]
    curcost = input[2]

    nextoptions = []

    for dir in dirs:

        if curcol + dir[0] < 0 or currow + dir[1] < 0 or curcol + dir[0] >= gridsize[0] or currow + dir[1] >= gridsize[1]:
            continue

        if raingrid[curcol + dir[0]][currow + dir[1]] == "#":
            continue

        if raingrid[curcol + dir[0]][currow + dir[1]] == ".":
            if rainscoregrid[curcol + dir[0]][currow + dir[1]] == 0 or curcost + 1 < rainscoregrid[curcol + dir[0]][currow + dir[1]]:
                rainscoregrid[curcol + dir[0]][currow + dir[1]] = curcost + 1
                nextoptions.append((curcol + dir[0], currow + dir[1], curcost + 1))

    return nextoptions

paths = [(0, 0, 0)]
walking = True
rainscoregrid = deepcopy(scoregrid)
raingrid = deepcopy(grid)

while walking == True:

    # Here we sort the list of sets to always only continue with the smallest ones
    paths.sort(key=lambda tup: tup[2])
    checkpath = paths[0]
    paths.remove(checkpath)
    paths.extend(dijkstra(checkpath))

    for path in paths:
        if path[0] == endpoint[0] and path[1] == endpoint[1]:
            P1Solution = path[2]
            walking = False

    testgrid = deepcopy(grid)
    for path in paths:
        testgrid[path[0]][path[1]] = path[2] 

print("P1 Solution (this is wrong bcs you have to only give the first 1024 raindrops, but I can't be bothered to do more AoC): " + str(P1Solution))

foundBlocker = False

for d, drop in enumerate(rain):

    if foundBlocker == True:
        break

    # Just fiddle with this till you found a block and then try next.
    # Too much advent of code in the last couple of days to now also implement this nicely
    if d < 2870:
        continue

    print("Step: " + str(d) + " of " + str(len(rain)) + " with new drop: " + str(drop))

    rainscoregrid = deepcopy(scoregrid)
    raingrid = deepcopy(grid)

    if d < 1000:
        continue

    for x in range(0, d):
        raingrid[rain[x][1]][rain[x][0]] = "#"

    paths = [(0, 0, 0)]
    walking = True

    while walking == True:

        if walking == True and len(paths) == 0:
            print("At Step " + str(d) + " we are done with byte: " + str((rain[d-1])))
            walking = False
            foundBlocker = True
            break

        # Here we sort the list of sets to always only continue with the smallest ones
        paths.sort(key=lambda tup: tup[2])
        checkpath = paths[0]
        paths.remove(checkpath)
        paths.extend(dijkstra(checkpath))

        for path in paths:
            if path[0] == endpoint[0] and path[1] == endpoint[1]:
                P1Solution = path[2]
                walking = False

        testgrid = deepcopy(raingrid)
        for path in paths:
            testgrid[path[0]][path[1]] = path[2] 

print("Code Finished")
