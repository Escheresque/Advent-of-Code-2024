from copy import deepcopy
import numpy as np
import os
import time

robots = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D14.txt") as file:
    for line in file:
        robot = {"spos": None, "vel": None, "curpos": None}
        workline = line.rstrip().replace("p=", "").replace("v=", "").replace(" ", ",").split(",")
        robot["spos"] = (int(workline[0]), int(workline[1]))
        robot["curpos"] = (int(workline[0]), int(workline[1]))
        robot["vel"] = (int(workline[2]), int(workline[3]))
        robots.append(robot)

hor = 101
ver = 103
seconds = 100

grid = []
for y in range(0, ver):
    temprow = []
    for x in range(0, hor):
        temprow.append(".")
    grid.append(temprow)

for robot in robots:

    xend = (robot["spos"][0] + (robot["vel"][0] * seconds)) % hor
    yend = (robot["spos"][1] + (robot["vel"][1] * seconds)) % ver
    robot["curpos"] = (xend, yend)

hcut = (len(grid) - 1) / 2
vcut = (len(grid[0]) - 1) / 2

robotsinspace = {"UL": 0, "UR": 0, "DL": 0, "DR": 0}

for robot in robots:

    x, y = robot["curpos"][0], robot["curpos"][1]

    if x < vcut and y < hcut: robotsinspace["UL"] += 1
    if x < vcut and y > hcut: robotsinspace["UR"] += 1
    if x > vcut and y < hcut: robotsinspace["DL"] += 1
    if x > vcut and y > hcut: robotsinspace["DR"] += 1

P1Solution = robotsinspace["UL"] * robotsinspace["UR"] * robotsinspace["DL"] * robotsinspace["DR"]

# Here we do part 2 - I figured that any picture would have some robots ("X") next to each other
for seconds in range(0, 100000):
    for robot in robots:

        xend = (robot["spos"][0] + (robot["vel"][0] * seconds)) % hor
        yend = (robot["spos"][1] + (robot["vel"][1] * seconds)) % ver
        robot["curpos"] = (xend, yend)

    grid = []
    for y in range(0, ver):
        temprow = []
        for x in range(0, hor):
            temprow.append(".")
        grid.append(temprow)

    for robot in robots:
        grid[robot["curpos"][1]][robot["curpos"][0]] = "X"

    FoundSecond= False
    print("Second: " + str(seconds) + " | ###########")
    for line in grid:
        String = "".join(map(str, line))
        if "XXXXXXXXXXXXXXXX" in String:
            FoundSecond = True

    if FoundSecond == True:
        for line in grid:
            print("".join(map(str, line)))
        print("P1 Solution: " + str(P1Solution))
        print("P2 Solution: " + str(seconds))
        break


