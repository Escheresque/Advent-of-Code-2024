
LeftList = []
RightList = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D1.txt") as file:
    for line in file:
        newLine = line.rstrip().split(" ")
        LeftList.append(int(newLine[0]))
        RightList.append(int(newLine[3]))

LeftList.sort()
RightList.sort()

SolList = []
for i, num in enumerate(LeftList):
    SolList.append(abs(RightList[i] - LeftList[i]))

print("Solution Part 1: " + str(sum(SolList)))

P2Sum = 0
for i, num in enumerate(LeftList):
    counter = 0

    for j, rnum in enumerate(RightList):

        if num == rnum:
            counter += 1

    P2Sum += num * counter

print("Day 1 Part 2 Solution: " + str(P2Sum))


