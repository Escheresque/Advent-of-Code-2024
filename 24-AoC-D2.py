
data = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D2.txt") as file:
    for line in file:
        temp = line.rstrip().split(" ")
        fill = []
        for num in temp:
            fill.append(int(num))
        data.append(fill)

def checkValid(line):

    valid = True
    asc = False
    desc = False

    for i in range(0, len(line) - 1):

        if abs(line[i] - line[i+1]) > 3:
            valid = False

        if line[i] == line[i+1]:
            valid = False

        if line[i] > line[i+1]:
            desc = True
        
        if line[i] < line[i+1]:
            asc = True

    if asc == True and desc == True:
        valid = False

    if valid == False:
        return 0
    elif valid == True:
        return 1

D2P1Solution = 0
D2P2Solution = 0

for line in data:

    D2P1Solution += checkValid(line)

    if checkValid(line) == 1:
        D2P2Solution += 1

    if checkValid(line) == 0:

        SafeLevels = False

        for i, num in enumerate(line):

            newLine = line.copy()
            newLine.pop(i)

            if checkValid(newLine) == 1:
                SafeLevels = True

        if SafeLevels == True:
            D2P2Solution += 1

print("D2 P1 Solution: " + str(D2P1Solution))
print("D2 P2 Solution: " + str(D2P2Solution))
print("--")


