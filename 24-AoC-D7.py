import re
import statistics
from copy import deepcopy

Results = []
Parts = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D7.txt") as file:
    for line in file:
        temp = line.rstrip().split(":")
        Results.append(int(temp[0]))
        Parts.append(list(map(int, temp[1].split(" ")[1:])))

def calctree(numlist, nexnum):

    newNums = []

    for num in numlist:

        nextmult = num * nexnum
        nextsum = num + nexnum
        nextcom = int(str(num) + str(nexnum))

        newNums.append(nextmult)
        newNums.append(nextsum)

        # Switch on for Part 2
        newNums.append(nextcom)

    return newNums

P1Solution = 0

for i, res in enumerate(Results):

    print(i)
    tree = [Parts[i][0]]

    for p in range(1, len(Parts[i])):

        tree = calctree(tree, Parts[i][p])

    if res in tree:
        P1Solution += res

print("P1 Solution: " + str(P1Solution))


    
        