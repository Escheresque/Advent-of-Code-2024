import re
import statistics
from copy import deepcopy
import numpy as np
import time

grid = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D10.txt") as file:
    for line in file:
        grid.append(list(line.rstrip()))

# this was for the test examples where not all symbols where ints
for i, row in enumerate(grid):
    for j, sym in enumerate(row):
        if sym != ".":
            grid[i][j] = int(sym)
        else:
            grid[i][j] = ""

# here we find the starting positions
trailheads = []
for i, row in enumerate(grid):
    for j, col in enumerate(grid[0]):
        if grid[i][j] == 0:
            trailheads.append((i,j))

# here we declare the bounds so that we don't hike of the grid
rowbound = len(grid[0])
colbound = len(grid)

# this function is basically our movement
def hike(i,j):

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    possibleways = set()

    for dir in directions:

        if (i + dir[0] < 0 or i + dir[0] >= colbound) or (j + dir[1] < 0 or j + dir[1] >= rowbound) or grid[i + dir[0]][j + dir[1]] == ".":
            continue

        else:
            nextstep = grid[i + dir[0]][j + dir[1]]

            if nextstep == grid[i][j] + 1:
                possibleways.add((i + dir[0], j + dir[1]))

    if len(possibleways) == 0:
        return 

    return possibleways

# this function is just a quick way to see if we reached a summit or not
def value(i, j):
    if grid[i][j] == 9:
        return "FIN"
    else:
        return (i, j)

starttime = time.time()
# P1 Solution - utilizing sets since we only want to find unique ends
P1Solution = 0
for trail in trailheads:

    posspos = [trail]

    while posspos.count("FIN") != len(posspos) and posspos:

        nextpos = set()

        for pos in posspos:

            if hike(pos[0], pos[1]) != None:
                if len(hike(pos[0], pos[1])) > 0:
                    for nextsteps in hike(pos[0], pos[1]):
                        nextpos.add(nextsteps)

        posspos = []
        for stuff in nextpos:
            posspos.append(value(stuff[0], stuff[1]))

    P1Solution += len(posspos)

print("P1 Solution: " + str(P1Solution) + " | Calculated in: " + str(time.time() - starttime))

starttime = time.time()
# Unfortunately, me being "smart" and using sets in P1 led to the need for a new P2
# We build the unique paths that lead to a summit and fill them in the completepaths list
completepaths = []
for trail in trailheads:

    paths = [[trail]]
    allFIN = False

    while allFIN == False:

        # remove paths that are already done
        paths = [p for p in paths if value(p[-1][0], p[-1][1]) != "FIN"]

        for i, path in enumerate(paths):

            nextsteps = hike(path[-1][0], path[-1][1])

            # here we test if next steps exist. if yes; append them to paths
            if nextsteps == None:
                continue

            if len(nextsteps) > 0:
                prevsteps = paths[i]
                for nextstep in nextsteps:
                    newpath = deepcopy(prevsteps)
                    newpath.append(nextstep)
                    paths.append(newpath)
                    currlen = len(newpath)

        # since either a path has come to an end or is one step further, we only want the further ones. This removes the shorter paths
        maxlen = 0
        for path in paths:
            if len(path) > maxlen:
                maxlen = len(path)
        paths = [p for p in paths if len(p) == maxlen]

        # here we check if the paths we currently have in path are finished. If yes, append them to completepaths, if no, continue with the while.
        allFIN = True
        for i, path in enumerate(paths):
            if value(path[-1][0], path[-1][1]) != "FIN":
                allFIN = False
            else:
                completepaths.append(path)

print("P2 Solution: " + str(len(completepaths)) + " | Calculated in: " + str(time.time() - starttime))





