import re
import statistics
from copy import deepcopy

Grid = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D6.txt") as file:
    for line in file:
        Grid.append(list(line.rstrip()))

dirs = [[-1, 0], [0, 1], [1, 0], [0,-1]]

for i in range(0,len(Grid)):
    for j in range(0, len(Grid[0])):
        if Grid[i][j] == "^":
            StartPosition = [i, j, 0, set()]

def movement(i, j, dirindex, vis, funcGrid):

    tryi = i + dirs[dirindex][0]
    tryj = j + dirs[dirindex][1]

    if (tryi < 0 or tryi >= len(Grid)) or (tryj < 0 or tryj >= len(Grid[0])):
        return "OUT"
    
    if (i, j, dirindex) in vis:
        return "LOOP"

    if funcGrid[tryi][tryj] == "#":

        vis.add((i, j, dirindex))
        return [i, j, (dirindex + 1) % 4, vis]
    
    else:

        nexti = i + dirs[dirindex][0]
        nextj = j + dirs[dirindex][1]

        return [nexti, nextj, dirindex, vis]
    
curPos = deepcopy(StartPosition)
TravelGrid = deepcopy(Grid)

while curPos != "OUT":

    TravelGrid[curPos[0]][curPos[1]] = "o"
    curPos = movement(curPos[0], curPos[1], curPos[2], set(), Grid)

P1Solution = 0
for i in range(0, len(TravelGrid)):
    for j in range(0, len(TravelGrid[0])):
        if TravelGrid[i][j] == "o":
            P1Solution += 1

P2Solution = 0
for i in range(0, len(TravelGrid)):
    for j in range(0, len(TravelGrid[0])):

        print("Coords: " + str(i) + "|" + str(j))
        curPos = deepcopy(StartPosition)
        tempGrid = deepcopy(Grid)

        if TravelGrid[i][j] == "o" and ((i, j) != (StartPosition[0], StartPosition[1])):

            tempGrid[i][j] = "#"
            visited = set()

            while curPos != "OUT" and curPos != "LOOP":

                tempGrid[curPos[0]][curPos[1]] = "o"
                curPos = movement(curPos[0], curPos[1], curPos[2], visited, tempGrid)
                
                if curPos == "LOOP":
                    P2Solution += 1

print("P1 Solution: " + str(P1Solution))
print("P2 Solution: " + str(P2Solution))
    
        