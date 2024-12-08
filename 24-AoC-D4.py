import re
import numpy as np

data = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D4.txt") as file:
    for line in file:
        data.append(line.rstrip())

transposed_data = []
for line in [[row[i] for row in data] for i in range(len(data[0]))]:
    transposed_data.append("".join(line))

def search_row(line):

    counter = 0

    for i in range(0,len(line) - 3):

        if line[i:i+4] == "XMAS":
            counter += 1

        if line[::-1][i:i+4] == "XMAS":
            counter += 1
    
    return counter

def search_diag(grid):

    counter = 0

    for i in range(0, len(grid) - 3):
        for j in range(0, len(grid[i]) - 3):

            if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3] == "XMAS":
                counter += 1

            if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3] == "SAMX":
                counter += 1

    for i in range(0, len(grid) - 3):
        for j in range(3, len(grid)):

            if grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3] == "XMAS":
                counter += 1

            if grid[i][j] + grid[i+1][j-1] + grid[i+2][j-2] + grid[i+3][j-3] == "SAMX":
                counter += 1

    return counter

D4P1Solution = 0
for i, line in enumerate(data):

    D4P1Solution += search_row(line)

for i, line in enumerate(transposed_data):
    D4P1Solution += search_row(line)

D4P1Solution += search_diag(data)

D4P2Solution = 0
for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):

        if data[i][j] == "A":

            print("Testing A | Row: " + str(i) + " & Col: " + str(j))
            teststring = data[i-1][j-1] + data[i-1][j+1] + data[i+1][j+1] + data[i+1][j-1]

            if teststring == "MSSM" or teststring == "MMSS" or teststring == "SMMS" or teststring == "SSMM":
                print("Coords | Row: " + str(i) + " & Col: " + str(j))
                D4P2Solution += 1

print("D2 P1 Solution: " + str(D4P1Solution))
print("D2 P2 Solution: " + str(D4P2Solution))


