import re
import statistics
from copy import deepcopy

# I am not proud of this one :)

string = ""
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D9.txt") as file:
    for line in file:
        string += line.rstrip()

input = list(string)

sollist = []
p2list = []
counter = 0

# First we create the needed lists - i create two for P1 and P2
for i, num in enumerate(input):

    if i % 2 == 0:

        sollist.extend(int(num) * [str(counter)])
        p2list.append(int(num) * [str(counter)])
        counter += 1

    else:

        sollist.extend(int(num) * ["."])
        p2list.append(int(num) * ["."])

onlynums = [v for v in sollist if v != "."]
dots = [d for d in sollist if d == "."]

# For P1 we just build the list from left to right.. if it is a number, take the number, if it is a dot, take the last number available.
# Since the length of the first and final string is the same, we can stop when we reached the final length
buildlist = []
counter = -1
for i, num in enumerate(sollist):
    if num != ".":
        buildlist.append(num)
    elif num == ".":
        buildlist.append(onlynums[counter])
        counter -= 1

    if len(buildlist) + len(dots) == len(sollist):
        break


# Here we get solution for P1
counter = 0
P1Solution = 0
for sym in list(buildlist):
    P1Solution += counter * int(sym)
    counter += 1

# Here we start P2
onlynumblocks = [b for b in p2list if not("." in b) and len(b) > 0]
onlydots = [d for d in p2list if "." in d]

blockpositions = []
for i, block in enumerate(p2list):
    if not("." in block) and len(block) > 0:
        blockpositions.append(i)

# Please do not ask me why this works, it does and thats enough.
worklist = deepcopy(p2list)
worklist = [w for w in worklist if w != []]
buildblocks = []
counter = -1
for n, numblock in enumerate(worklist[::-1]):
    if "." in numblock: continue
    print(numblock)
    for i, block in enumerate(worklist):
        if block == numblock:
            break
        if "." in block and len(block) >= len(numblock):
            newblocks = numblock, list((len(block)-len(numblock))*".")
            worklist.pop(i)
            worklist[i:i] = newblocks
            worklist[len(worklist) - 1 - worklist[::-1].index(numblock)] = list(len(numblock)*".")
            worklist = [w for w in worklist if w != []]
            
            # Clean up: if we have stuff like .., ["."], [".", "."], ["."],.. in our list, we make ..., [".",".",".","."], ... out of it
            for i in range(0, len(worklist) - 1):
                if i+1 >= len(worklist): break
                if "." in worklist[i]:
                    dotcounter = len(worklist[i])
                    j = 0
                    while "." in worklist[i+1+j]:
                        if i+1+j >= len(worklist): break
                        dotcounter += len(worklist[i+j+1])
                        j += 1
                        if i+1+j >= len(worklist): break
                    if j == 0:
                        worklist[i] = list(dotcounter * ".")
                    if j > 0:
                        testlist = list(dotcounter * ".")
                        worklist[i:i+j+1] = [testlist]

            break

# make sub list
endlist = []
for block in worklist:
    endlist.extend(block)

counter = 0
P2Solution = 0
for sym in endlist:
    if sym == ".":
        P2Solution += 0
        counter += 1
    else:
        P2Solution += counter * int(sym)
        counter += 1
    print("symbol: " + str(sym) + " | counter: " + str(counter) + " | new P2Sol: " + str(P2Solution))
    print("")

print("P1 Solution: " + str(P1Solution))
print("P2 Solution: " + str(P2Solution))




