from copy import deepcopy
import numpy as np
import pandas as pd
import os
import time
from operator import itemgetter

grid = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D16.txt") as file:
    for line in file:
        grid.append(list(line.rstrip()))

AlreadyVisited = set()
for i, row in enumerate(grid):
    for j, pos in enumerate(grid[i]):
        if pos == "S":
            StartPos = (i, j, "E", 0)
            AlreadyVisited.add((i, j))
        elif pos == "E":
            EndPos = (i, j)

dirs = {"N": (-1, 0), "E": (0, 1), "S": (1, 0), "W": (0, -1)}
paths = [{"Visited": [(StartPos[0], StartPos[1], "E")], "Path": [StartPos]}]
foundEnd = False

def dijkstrastep(path, visited):

    global foundEnd
    global solpathcost

    rowpos = path[-1][0]
    colpos = path[-1][1]
    facing = path[-1][2]
    cost = path[-1][3]

    # First we check the next possible steps:

    nextoptions = []
    for dir in dirs.keys():
        if grid[rowpos + dirs[dir][0]][colpos + dirs[dir][1]] == "#":
            continue
        elif (rowpos + dirs[dir][0], colpos + dirs[dir][1], facing) in visited:
             continue
        elif grid[rowpos + dirs[dir][0]][colpos + dirs[dir][1]] == "E":
            newpath = deepcopy(path)
            newvisited = deepcopy(visited)
            newpath.append((rowpos + dirs[dir][0], colpos + dirs[dir][1], facing, cost + 1))
            newvisited.append((rowpos + dirs[dir][0], colpos + dirs[dir][1], facing))
            nextoptions.append({"Visited": newvisited, "Path": newpath})
            solpathcost = cost + 1
            foundEnd = True
        elif dir == facing:
            newpath = deepcopy(path)
            newvisited = deepcopy(visited)
            newpath.append((rowpos + dirs[dir][0], colpos + dirs[dir][1], facing, cost + 1))
            newvisited.append((rowpos + dirs[dir][0], colpos + dirs[dir][1], facing))
            nextoptions.append({"Visited": newvisited, "Path": newpath})
        elif dir != facing:
            newpath = deepcopy(path)
            newvisited = deepcopy(visited)
            newpath.append((rowpos + dirs[dir][0], colpos + dirs[dir][1], dir, cost + 1001))
            newvisited.append((rowpos + dirs[dir][0], colpos + dirs[dir][1], facing))
            nextoptions.append({"Visited": newvisited, "Path": newpath})

    return nextoptions

scoregrid = deepcopy(grid)
for i, row in enumerate(scoregrid):
    for j, col in enumerate(scoregrid[i]):
        if scoregrid[i][j] != "#":
            scoregrid[i][j] = {"N": 80000, "E": 80000, "S": 80000, "W": 80000}

finishedPaths = []
solpathcost = 0
StillOtherPaths = True
while StillOtherPaths == True:

    mincost = 99999999999999999999999999
    for p, path in enumerate(paths):
        laststep = path["Path"][-1][3]
        if laststep < mincost:
            mincost = laststep
            nextpath = deepcopy(p)
    
    print(str(len(paths)) + " MinCost: " + str(mincost))

    funcreturn = dijkstrastep(paths[nextpath]["Path"], paths[nextpath]["Visited"])
            
    if len(funcreturn) == 0:
        paths.pop(nextpath)
    elif len(funcreturn[0]) == 1:
        paths[nextpath] = funcreturn
    else:
        paths.pop(nextpath)
        for nextpaths in funcreturn:
            paths.append(nextpaths)

    removePaths = []
    for path in paths:
        if path["Path"][-1][3] > scoregrid[path["Path"][-1][0]][path["Path"][-1][1]][path["Path"][-1][2]]:
            removePaths.append(path)
        else:
            scoregrid[path["Path"][-1][0]][path["Path"][-1][1]][path["Path"][-1][2]] = path["Path"][-1][3]

    for path in removePaths:
        paths.remove(path)

    tgrid = deepcopy(grid)
    for path in paths:
        tgrid[path["Path"][-1][0]][path["Path"][-1][1]] = path["Path"][-1][3]


    if solpathcost != 0:
        removePaths = []
        for p, path in enumerate(paths):
            if path["Path"][-1][3] == solpathcost and path["Path"][-1][0] == EndPos[0] and path["Path"][-1][1] == EndPos[1]:
                finishedPaths.append(path)
            if path["Path"][-1][3] > solpathcost:
                removePaths.append(path)

        for path in removePaths:
            paths.remove(path)

        StillOtherPaths = False
        if len(paths) > 0:
            StillOtherPaths = True

shortestPaths = []
for path in finishedPaths:
    if path["Path"][-1][0] == EndPos[0] and path["Path"][-1][1] == EndPos[1] and path["Path"][-1][3] == solpathcost:
        shortestPaths.append(path)

testgrid = deepcopy(grid)
for path in shortestPaths:
    for step in path["Path"]:
        testgrid[step[0]][step[1]] = "O"

P2Solution = 0
for i, row in enumerate(testgrid):
    for j, col in enumerate(testgrid[0]):
        if testgrid[i][j] == "O":
            P2Solution += 1

P1Solution = shortestPaths[0]["Path"][-1][3]
print("P1 Solution: " + str(P1Solution))
print("P2 Solution: " + str(P2Solution))


