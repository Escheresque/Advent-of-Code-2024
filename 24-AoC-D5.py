import re
import statistics

Rules = []
Pages = []
skip = False
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D5.txt") as file:
    for line in file:
        if skip == False and line.rstrip() != "":
            Rules.append(line.rstrip().split("|"))
        elif skip == True and line != "":
            Pages.append(line.rstrip().split(","))
            
        if line.rstrip() == "":
            skip = True

CorrectOrders = []
FalseOrders = []

for pine in Pages:

    OrderCorrect = True

    for i, p in enumerate(pine):

        for others in pine[i+1:]:

            for rule in Rules:

                if rule[0] == others and rule[1] == p:

                    OrderCorrect = False

    
    if OrderCorrect == True:
        CorrectOrders.append(pine)
    if OrderCorrect == False:
        FalseOrders.append(pine)

P1Solution = 0
for sols in CorrectOrders:
    middleint = len(sols)//2
    P1Solution += int(sols[int(middleint)])

print("Starting P2")

# I apologize for this solution and I'm actually surprised, that it works at all. 
# But hey, it ain't stupid if it works, right?

P2Solution = 0

for orders in FalseOrders:

    currRules = []

    for rule in Rules:
        if rule[0] in orders and rule[1] in orders:
            currRules.append(rule)

    positionIndicators = []

    for ord in orders:
        
        position = 0

        for crule in currRules:
            if ord == crule[0]:
                position += 1

        positionIndicators.append(position)

    for i, ind in enumerate(positionIndicators):
        if ind == statistics.median(positionIndicators):
            P2Solution += int(orders[i])



print(P1Solution)
print(P2Solution)

