from copy import deepcopy
import numpy as np

gamesraw = []
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D13.txt") as file:
    for line in file:
        gamesraw.append(line.rstrip())

gamesclean = []
for i in range(0, len(gamesraw), 4):
        game = {"s": None, "a": None, "b": None, "sol": None, "solCost": None}
        line1 = gamesraw[i].rstrip().split()
        line2 = gamesraw[i+1].rstrip().split()
        line3 = gamesraw[i+2].rstrip().split()
        game["s"] = [int(line3[1].split("=")[1][:-1]), int(line3[2].split("=")[1])]
        game["a"] = [int(line1[2].split("+")[1][:-1]), int(line1[3].split("+")[1])]
        game["b"] = [int(line2[2].split("+")[1][:-1]), int(line2[3].split("+")[1])]
        gamesclean.append(game)

cost = {"a": 3, "b": 1}

P1Solution = 0
for game in gamesclean:

    s0 = game["s"][0]
    s1 = game["s"][1]
    a0 = game["a"][0]
    a1 = game["a"][1]
    b0 = game["b"][0]
    b1 = game["b"][1]
     
    A = (s0 * b1 - s1 * b0) / (a0 * b1 - a1 * b0)
    B = (s0 * a1 - s1 * a0) / (b0 * a1 - b1 * a0)

    if A < 101 and B < 101 and A >= 0 and B >= 0 and round(A) == A and round(B) == B:
        game["sol"] = [A, B]
        game["solCost"] = A * cost["a"] + B * cost["b"]
        P1Solution += game["solCost"]

P2Solution = 0
for game in gamesclean:

    s0 = game["s"][0] + 10000000000000
    s1 = game["s"][1] + 10000000000000
    a0 = game["a"][0]
    a1 = game["a"][1]
    b0 = game["b"][0]
    b1 = game["b"][1]
     
    A = (s0 * b1 - s1 * b0) / (a0 * b1 - a1 * b0)
    B = (s0 * a1 - s1 * a0) / (b0 * a1 - b1 * a0)

    if A >= 0 and B >= 0 and round(A) == A and round(B) == B:
        game["sol"] = [A, B]
        game["solCost"] = A * cost["a"] + B * cost["b"]
        P2Solution += game["solCost"]

print("P1 Solution: " + str(P1Solution))
print("P2 Solution: " + str(P2Solution))
