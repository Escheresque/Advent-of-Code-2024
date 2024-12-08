import re
import statistics
from copy import deepcopy

grid = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D8.txt") as file:
    for line in file:
        grid.append(list(line.rstrip()))

gridboundrow = len(grid) 
gridboundcol = len(grid[0])

# First find locations of different nodes:
antennalocs = {}

for i, row in enumerate(grid):
    for j,loc in enumerate(row):
        if loc != ".":
            if loc in antennalocs.keys():
                antennalocs[loc].append((i, j))
            else:
                antennalocs[loc] = [(i,j)]

# Part 1
antinodeLocations = []
for key in antennalocs.keys():
     
    keyNodes = antennalocs[key]

    for n, node1 in enumerate(keyNodes):
        for m in range(n + 1, len(keyNodes)):
             
            node2 = keyNodes[m]

            dist = [node1[0] - node2[0], node1[1] - node2[1]]

            antinode1 = [(node1[0] + dist[0]), (node1[1] + dist[1])]
            antinode2 = [(node2[0] - dist[0]), (node2[1] - dist[1])]

           # Now we check if we are in bounds
            if (antinode1[0] >= 0 and antinode1[0] < gridboundrow) and (antinode1[1] >= 0 and antinode1[1] < gridboundcol):
                antinodeLocations.append(antinode1)

            if (antinode2[0] >= 0 and antinode2[0] < gridboundrow) and (antinode2[1] >= 0 and antinode2[1] < gridboundcol):
                antinodeLocations.append(antinode2)

uniquelocs = [list[x] for x in set(tuple(x) for x in antinodeLocations)]
P1Solution = len(uniquelocs)
print("P1 Solution: " + str(P1Solution))

# Part 2
antinodeLocations = []
for key in antennalocs.keys():
    keyNodes = antennalocs[key]

    for n, node1 in enumerate(keyNodes):
        for m in range(n + 1, len(keyNodes)):

            node2 = keyNodes[m]

            dist = [node1[0] - node2[0], node1[1] - node2[1]]

            for mul in range(0, 99):

                antinode1 = [(node1[0] + mul * dist[0]), (node1[1] + mul * dist[1])]
                antinode2 = [(node2[0] - mul * dist[0]), (node2[1] - mul * dist[1])]

                # Now we check if we are in bounds
                if (antinode1[0] >= 0 and antinode1[0] < gridboundrow) and (antinode1[1] >= 0 and antinode1[1] < gridboundcol):
                    antinodeLocations.append(antinode1)

                if (antinode2[0] >= 0 and antinode2[0] < gridboundrow) and (antinode2[1] >= 0 and antinode2[1] < gridboundcol):
                    antinodeLocations.append(antinode2)

uniquelocs2 = [list[x] for x in set(tuple(x) for x in antinodeLocations)]
P2Solution = len(uniquelocs2)
print("P2 Solution: " + str(P2Solution))

copygrid = deepcopy(grid)
for i, j in antinodeLocations:
    copygrid[i][j] = "#"

print(list(range(0,5)))
