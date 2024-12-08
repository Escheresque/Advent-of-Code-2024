import re

data = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D3.txt") as file:
    for line in file:
        data.append(line)

fulltext = "S"

for line in data:
    fulltext = fulltext + line

D2P1Solution = 0
D2P2Solution = 0

for line in data:
    calcs = re.findall(r"mul\(\d*\,\d*\)", line)

    for mul in calcs:
        temp = re.findall(r"\d+", mul)

        product = 1
        for digit in temp:
            product = product * int(digit)

        D2P1Solution += product


work = fulltext.split("do()")

for segment in work:

    work2 = segment.split("don't()")[0]
        
    calcs2 = re.findall(r"mul\(\d*\,\d*\)", work2)

    for mul in calcs2:
        temp = re.findall(r"\d+", mul)

        product = 1
        for digit in temp:
            product = product * int(digit)

        D2P2Solution += product

print("D2 P1 Solution: " + str(D2P1Solution))
print("D2 P2 Solution: " + str(D2P2Solution))


