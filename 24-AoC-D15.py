from copy import deepcopy
import numpy as np
import os
import time

grid = []
movement = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D15.txt") as file:
    for line in file:
        if line == '\n':
            continue
        elif "#" == list(line.rstrip())[0]:
            grid.append(list(line.rstrip()))
        else:
            movement.extend(list(line.rstrip()))

newgrid = []
for i, row in enumerate(grid):
    temprow = []
    for j, pos in enumerate(grid[i]):
        if pos == "#":
            temprow.extend(["#", "#"])
        elif pos == "O":
            temprow.extend(["[", "]"])
        elif pos == ".":
            temprow.extend([".", "."])
        elif pos == "@":
            temprow.extend(["@", "."])
    newgrid.append(temprow)

moves = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}

for i, row in enumerate(grid):
    for j, pos in enumerate(grid[0]):
        if grid[i][j] == "@":
            robpos = (i, j)

for i, row in enumerate(newgrid):
    for j, pos in enumerate(newgrid[0]):
        if newgrid[i][j] == "@":
            p2robpos = (i, j)

def robmove(robpos, curgrid, mov):

    workgrid = deepcopy(curgrid)
    nextspace = curgrid[robpos[0] + moves[mov][0]][robpos[1] + moves[mov][1]]

    if nextspace == ".":
        workgrid[robpos[0]][robpos[1]] = "."
        workgrid[robpos[0] + moves[mov][0]][robpos[1] + moves[mov][1]] = "@"
        newrobpos = (robpos[0] + moves[mov][0], robpos[1] + moves[mov][1])
        return newrobpos, workgrid

    elif nextspace == "#":
        return robpos, curgrid

    elif nextspace == "O":

        boxcounter = 1
        while curgrid[robpos[0] + moves[mov][0] * (1 + boxcounter)][robpos[1] + moves[mov][1] * (1 + boxcounter)] != "." and curgrid[robpos[0] + moves[mov][0] * (1 + boxcounter)][robpos[1] + moves[mov][1] * (1 + boxcounter)] != "#":
            boxcounter += 1

        if curgrid[robpos[0] + moves[mov][0] * (1 + boxcounter)][robpos[1] + moves[mov][1] * (1 + boxcounter)] == "#":
            return robpos, curgrid

        elif curgrid[robpos[0] + moves[mov][0] * (1 + boxcounter)][robpos[1] + moves[mov][1] * (1 + boxcounter)] == ".":
            workgrid[robpos[0]][robpos[1]] = "."
            workgrid[robpos[0] + moves[mov][0]][robpos[1] + moves[mov][1]] = "@"
            workgrid[robpos[0] + moves[mov][0] * (1 + boxcounter)][robpos[1] + moves[mov][1] * (1 + boxcounter)] = "O"
            newrobpos = (robpos[0] + moves[mov][0], robpos[1] + moves[mov][1])
            return newrobpos, workgrid
        
def robmovep2(robpos, curgrid, mov, m):
    
    workgrid = deepcopy(curgrid)
    nextspace = curgrid[robpos[0] + moves[mov][0]][robpos[1] + moves[mov][1]]
    nextspacecoord = (robpos[0] + moves[mov][0], robpos[1] + moves[mov][1])
    newrobpos = (robpos[0] + moves[mov][0], robpos[1] + moves[mov][1])

    if nextspace == ".":
        workgrid[robpos[0]][robpos[1]] = "."
        workgrid[robpos[0] + moves[mov][0]][robpos[1] + moves[mov][1]] = "@"
        newrobpos = (robpos[0] + moves[mov][0], robpos[1] + moves[mov][1])
        return newrobpos, workgrid

    elif nextspace == "#":
        return robpos, curgrid

    elif nextspace == "[" or nextspace == "]":

        if nextspace == "[":
            pushedboxes = [[nextspacecoord, (nextspacecoord[0], nextspacecoord[1] + 1)]]
        elif nextspace == "]":
            pushedboxes = [[(nextspacecoord[0], nextspacecoord[1] - 1), nextspacecoord]]

        noMoreBoxes = False
        alreadychecked = []
        while noMoreBoxes == False:

            oldpushboxes = deepcopy(pushedboxes)

            for box in oldpushboxes:

                if box in alreadychecked:
                    continue

                boxl = box[0]
                boxr = box[1]

                if mov == "^":

                    if curgrid[boxl[0] - 1][boxl[1]] == "." and curgrid[boxr[0] - 1][boxr[1]] == ".":
                        continue
                    elif curgrid[boxl[0] - 1][boxl[1]] == "]" and curgrid[boxr[0] - 1][boxr[1]] == ".":
                        pushedboxes.append([(boxl[0] - 1, boxl[1] - 1), (boxl[0] - 1, boxl[1])])
                    elif curgrid[boxl[0] - 1][boxl[1]] == "." and curgrid[boxr[0] - 1][boxr[1]] == "[":
                        pushedboxes.append([(boxr[0] - 1, boxr[1]), (boxr[0] - 1, boxr[1] + 1)])
                    elif curgrid[boxl[0] - 1][boxl[1]] == "]" and curgrid[boxr[0] - 1][boxr[1]] == "[":
                        pushedboxes.append([(boxl[0] - 1, boxl[1] - 1), (boxl[0] - 1, boxl[1])])
                        pushedboxes.append([(boxr[0] - 1, boxr[1]), (boxr[0] - 1, boxr[1] + 1)])
                    elif curgrid[boxl[0] - 1][boxl[1]] == "[" and curgrid[boxr[0] - 1][boxr[1]] == "]":
                        pushedboxes.append([(boxl[0] - 1, boxl[1]), (boxr[0] - 1, boxr[1])])

                    alreadychecked.append(box)
                                        
                elif mov == ">":

                    if curgrid[boxr[0]][boxr[1] + 1] == ".":
                        continue
                    elif curgrid[boxr[0]][boxr[1] + 1] == "[":
                        pushedboxes.append([(boxr[0], boxr[1] + 1), (boxr[0], boxr[1] + 2)])

                    alreadychecked.append(box)

                elif mov == "<":
                    if curgrid[boxl[0]][boxl[1] - 1] == ".":
                        continue
                    elif curgrid[boxl[0]][boxl[1] - 1] == "]":
                        pushedboxes.append([(boxl[0], boxl[1] - 2), (boxl[0], boxl[1] - 1)])

                    alreadychecked.append(box)

                elif mov == "v":

                    if curgrid[boxl[0] + 1][boxl[1]] == "." and curgrid[boxr[0] + 1][boxr[1]] == ".":
                        continue
                    elif curgrid[boxl[0] + 1][boxl[1]] == "]" and curgrid[boxr[0] + 1][boxr[1]] == ".":
                        pushedboxes.append([(boxl[0] + 1, boxl[1] - 1), (boxl[0] + 1, boxl[1])])
                    elif curgrid[boxl[0] + 1][boxl[1]] == "." and curgrid[boxr[0] + 1][boxr[1]] == "[":
                        pushedboxes.append([(boxr[0] + 1, boxr[1]), (boxr[0] + 1, boxr[1] + 1)])
                    elif curgrid[boxl[0] + 1][boxl[1]] == "]" and curgrid[boxr[0] + 1][boxr[1]] == "[":
                        pushedboxes.append([(boxl[0] + 1, boxl[1] - 1), (boxl[0] + 1, boxl[1])])
                        pushedboxes.append([(boxr[0] + 1, boxr[1]), (boxr[0] + 1, boxr[1] + 1)])
                    elif curgrid[boxl[0] + 1][boxl[1]] == "[" and curgrid[boxr[0] + 1][boxr[1]] == "]":
                        pushedboxes.append([(boxl[0] + 1, boxl[1]), (boxr[0] + 1, boxr[1])])

                    alreadychecked.append(box)

            if oldpushboxes == pushedboxes:
                noMoreBoxes = True

        validPush = True
        for box in pushedboxes:

            if mov == "^":
                if curgrid[box[0][0] - 1][box[0][1]] == "#" or curgrid[box[1][0] - 1][box[1][1]] == "#":
                    validPush = False

            elif mov == "v":
                if curgrid[box[0][0] + 1][box[0][1]] == "#" or curgrid[box[1][0] + 1][box[1][1]] == "#":
                    validPush = False

            elif mov == ">":
                if curgrid[box[1][0]][box[1][1] + 1] == "#":
                    validPush = False

            elif mov == "<":
                if curgrid[box[0][0]][box[0][1] - 1] == "#":
                    validPush = False

        if validPush == False:
            return robpos, curgrid
        
        elif validPush == True:

            if mov == "<":
                for box in pushedboxes[::-1]:
                    boxl = box[0]
                    boxr = box[1]
                    workgrid[boxl[0]][boxl[1]] = "."
                    workgrid[boxr[0]][boxr[1]] = "."
                    workgrid[boxl[0]][boxl[1] - 1] = "["
                    workgrid[boxr[0]][boxr[1] - 1] = "]"

            elif mov == ">":
                for box in pushedboxes[::-1]:
                    boxl = box[0]
                    boxr = box[1]
                    workgrid[boxl[0]][boxl[1]] = "."
                    workgrid[boxr[0]][boxr[1]] = "."
                    workgrid[boxl[0]][boxl[1] + 1] = "["
                    workgrid[boxr[0]][boxr[1] + 1] = "]"

            elif mov == "^":
                for box in pushedboxes[::-1]:

                    boxl = box[0]
                    boxr = box[1]
                    workgrid[boxl[0]][boxl[1]] = "."
                    workgrid[boxr[0]][boxr[1]] = "."
                    workgrid[boxl[0] - 1][boxl[1]] = "["
                    workgrid[boxr[0] - 1][boxr[1]] = "]"


            elif mov == "v":
                for box in pushedboxes[::-1]:
                    boxl = box[0]
                    boxr = box[1]
                    workgrid[boxl[0]][boxl[1]] = "."
                    workgrid[boxr[0]][boxr[1]] = "."
                    workgrid[boxl[0] + 1][boxl[1]] = "["
                    workgrid[boxr[0] + 1][boxr[1]] = "]"

            workgrid[robpos[0]][robpos[1]] = "."
            workgrid[newrobpos[0]][newrobpos[1]] = "@"
            

            return newrobpos, workgrid

def getind(boxes, mov):

    if mov == ">":
        larg = 0
        for box in boxes:
            if box[1][1] > larg: larg = box[1][1]
        return larg

    elif mov == "<":
        mins = 9999999
        for box in boxes:
            if box[0][1] < mins: mins = box[0][1]
        return mins
    
    elif mov == "^":
        mins = 9999999
        for box in boxes:
            if box[0][0] < mins: mins = box[0][0]
        return mins

    elif mov == "v":
        larg = 0
        for box in boxes:
            if box[0][0] > larg: larg = box[0][0]
        return larg

curgrid = deepcopy(grid)       
for m, move in enumerate(movement):
    if m % 1000 == 0:
        print("Current P1 Step: " + str(m) + " of " + str(len(movement)))
    robpos, curgrid = robmove(robpos, curgrid, move)

P1Solution = 0
for i, row in enumerate(curgrid):
    for j, pos in enumerate(curgrid[0]):
        if curgrid[i][j] == "O":
            P1Solution += i * 100 + j 

p2curgrid = deepcopy(newgrid)
for m, move in enumerate(movement):

    if m % 1000 == 0:
        print("Current P2 Step: " + str(m) + " of " + str(len(movement)))

    # with open('Test.txt', 'w') as f:
    #     if p2curgrid[p2robpos[0] + moves[move][0]][p2robpos[1] + moves[move][1]] == "]" or p2curgrid[p2robpos[0] + moves[move][0]][p2robpos[1] + moves[move][1]] == "[":
    #         p2curgrid[p2robpos[0]][p2robpos[1]] = move
            

    #     f.write("RobPos" + str(p2robpos) + " | P2 Move: " + str(m) + " / " + str(len(movement)) + "| Dir: " + str(move) + " | Next Space: " + str(p2curgrid[p2robpos[0] + moves[move][0]][p2robpos[1] + moves[move][1]]) + str('\n'))
    #     for l, line in enumerate(p2curgrid):
    #         f.write("".join(line) + str('\n'))

    # if p2curgrid[p2robpos[0] + moves[move][0]][p2robpos[1] + moves[move][1]] == "]" or p2curgrid[p2robpos[0] + moves[move][0]][p2robpos[1] + moves[move][1]] == "[":
    #     time.sleep(0)

    prevgrid = deepcopy(p2curgrid)
    p2robpos, p2curgrid = robmovep2(p2robpos, p2curgrid, move, m)

    # time.sleep(0)

P2Solution = 0
for i, row in enumerate(p2curgrid):
    for j, pos in enumerate(p2curgrid[0]):
        if p2curgrid[i][j] == "[":
            P2Solution += i * 100 + j

with open('Test.txt', 'w') as f:
    for line in p2curgrid:
        f.write("".join(line) + str('\n'))

print("P1 Solution: " + str(P1Solution))
print("P2 Solution: " + str(P2Solution))
print("-")
