from copy import deepcopy
import numpy as np

grid = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D12.txt") as file:
    for line in file:
        grid.append(list(line.rstrip()))

rowbound = len(grid[0])
colbound = len(grid)

# this function finds a whole region. 
# We check the neighbors: if they fit and we haven't seen them yet, they are added to the region.
# we also add them to a totalchecked that we don't have to check again
def findregion(curregion):

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    testregion = deepcopy(curregion)

    for (i, j) in testregion:

        currsym = grid[i][j]

        for dir in dirs:
            if (i + dir[0] < 0 or i + dir[0] >= colbound) or (j + dir[1] < 0 or j + dir[1] >= rowbound):
                continue
            else:
                if grid[i + dir[0]][j + dir[1]]  == currsym and not((i + dir[0],j + dir[1]) in curregion):
                    curregion.append((i + dir[0], j + dir[1]))
                    totalchecked.append((i + dir[0], j + dir[1]))

    totalchecked.append((i, j))

    return curregion

# Here we check which fences a specific coordinate has. 
# First we check if it is at a bound -> add the 1s
# if not in bound and it has not the same symbol next to it -> add a 1
def findfences(i, j):

    currsym = grid[i][j]
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    fences = {"N": 0, "E": 0, "S": 0, "W": 0}

    for dir in dirs:
            
            if (i + dir[0] < 0): fences["N"] = 1
            if (i + dir[0] >= colbound): fences["S"] = 1
            if (j + dir[1] < 0): fences["W"] = 1
            if (j + dir[1] >= rowbound): fences["E"] = 1

    if fences["N"] != 1 and grid[i-1][j] != currsym: fences["N"] = 1
    if fences["E"] != 1 and grid[i][j+1] != currsym: fences["E"] = 1
    if fences["S"] != 1 and grid[i+1][j] != currsym: fences["S"] = 1
    if fences["W"] != 1 and grid[i][j-1] != currsym: fences["W"] = 1

    return fences

# Here we check the regions
totalchecked = []
regionlist = []
for i, row in enumerate(grid):
    for j, col in enumerate(grid[0]):

        curregion = [(i, j)]

        if not((i, j) in totalchecked):

            RegionDone = False
            while RegionDone == False:

                oldregion = deepcopy(curregion)
                curregion = findregion(curregion)      

                if len(oldregion) == len(curregion):
                    RegionDone = True

            regionlist.append(curregion)

# here we find the fences for every coord
fencegrid = deepcopy(grid)
for i, row in enumerate(grid):
    for j, col in enumerate(grid[0]):
        fencegrid[i][j] = findfences(i, j)

# Here we now look at our regions and count the fences per region to multiply it and to get the result
P1Solution = 0
for region in regionlist:
    fenceamount = 0
    for coord in region:
        fenceamount += sum(fencegrid[coord[0]][coord[1]].values())

    P1Solution += len(region) * fenceamount

########################################################################################################################

# This function looks scary but it is really not so bad
# Let's stick as an example with the sorted list of coords that have northern fences
# We start at one coord -> if the one right next to it also has a norther fence, this is one more, and so on
# we add fences that we have already checked to a list, so that we don't count them more than one time
# when this "check the right next"-coord breaks, we check the other fences that have northern fence
# etc. 
def checklongfences(X_Sorted, X):

    X_Fences = []
    X_Checked_Fences = []

    for i, coord in enumerate(X_Sorted):

        if coord in X_Checked_Fences:
            continue
        else:
            curFence = [coord]
            X_Checked_Fences.append(coord)

        startrow = coord[0]
        startcol = coord[1]
        currow = coord[0]
        curcol = coord[1]

        for j in range(i+ 1, len(X_Sorted)):

            if X_Sorted[j] in X_Checked_Fences:
                continue

            if X == "N" and X_Sorted[j][0] == startrow and X_Sorted[j][1] == curcol + 1:
                X_Checked_Fences.append(X_Sorted[j])
                curFence.append(X_Sorted[j])
                curcol += 1

            if X == "E" and X_Sorted[j][1] == startcol and X_Sorted[j][0] == currow + 1:
                X_Checked_Fences.append(X_Sorted[j])
                curFence.append(X_Sorted[j])
                currow += 1

            if X == "S" and X_Sorted[j][0] == startrow and X_Sorted[j][1] == curcol + 1:
                X_Checked_Fences.append(X_Sorted[j])
                curFence.append(X_Sorted[j])
                curcol += 1

            if X == "W" and X_Sorted[j][1] == startcol and X_Sorted[j][0] == currow + 1:
                X_Checked_Fences.append(X_Sorted[j])
                curFence.append(X_Sorted[j])
                currow += 1

        X_Fences.append(curFence)

    return X_Fences

P2Solution = 0

# Here we go for part 2 -> we go through every region in region list
# and we check which coords have a fence at which side. 
# If there is a fence at a side, we add the coord to the regionfencing dict
for region in regionlist:

    # In this dict we add the coords that have a fence on the specific side
    regionfencing = {"N": [], "E": [], "S": [], "W": []}

    # here we add the coords to regionfencing
    for coord in region:

        if fencegrid[coord[0]][coord[1]]["N"] == 1: regionfencing["N"].append(coord)
        if fencegrid[coord[0]][coord[1]]["E"] == 1: regionfencing["E"].append(coord)
        if fencegrid[coord[0]][coord[1]]["S"] == 1: regionfencing["S"].append(coord)
        if fencegrid[coord[0]][coord[1]]["W"] == 1: regionfencing["W"].append(coord)

    # here we sort the coords that have north, east, south, west fences -> we need this for the function that checks how many long fences we have
    N_Sorted = sorted(regionfencing["N"], key=lambda element: (element[0], element[1]))
    E_Sorted = sorted(regionfencing["E"], key=lambda element: (element[0], element[1]))
    S_Sorted = sorted(regionfencing["S"], key=lambda element: (element[0], element[1]))
    W_Sorted = sorted(regionfencing["W"], key=lambda element: (element[0], element[1]))

    # The function checklongfences then gives us how many long fences we have for each direction
    N_Fences = checklongfences(N_Sorted, "N")
    E_Fences = checklongfences(E_Sorted, "E")
    S_Fences = checklongfences(S_Sorted, "S")
    W_Fences = checklongfences(W_Sorted, "W")

    # And calc the solution
    fenceamount = len(N_Fences) + len(E_Fences) + len(S_Fences) + len(W_Fences)
    P2Solution += len(region) * fenceamount

print("P1 Solution: " + str(P1Solution))
print("P2 Solution: " + str(P2Solution))
