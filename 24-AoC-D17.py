from copy import deepcopy
import numpy as np
import pandas as pd
import os
import time
from operator import itemgetter

Reg = {"A": None, "B": None, "C": None}
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D17.txt") as file:
    for l, line in enumerate(file):
        if l == 0:
            Reg["A"] = int(list(line.rstrip().split(" "))[-1])
        if l == 1:
            Reg["B"] = int(list(line.rstrip().split(" "))[-1])
        if l == 2:
            Reg["C"] = int(list(line.rstrip().split(" "))[-1])
        if l == 4:
            newline = line.rstrip().replace("Program: ", "")
            Program = list(map(int, newline.split(",")))

curropcode = Program[0]
curroperand = Program[1]

instruction_pointer = 0

combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: Reg["A"], 5: Reg["B"], 6: Reg["C"], 7: None}

def opcode0_adv(coperand):
    global instruction_pointer
    global Reg
    combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: Reg["A"], 5: Reg["B"], 6: Reg["C"], 7: None}

    result = int(Reg["A"] / (pow(2, combo_operands[coperand])))
    Reg["A"] = int(result)
    instruction_pointer += 2

def opcode1_bxl(lit_operand):
    global instruction_pointer
    global Reg
    combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: Reg["A"], 5: Reg["B"], 6: Reg["C"], 7: None}

    result = Reg["B"] ^ lit_operand
    Reg["B"] = result
    instruction_pointer += 2

def opcode2_bst(coperand):
    global instruction_pointer
    global Reg
    combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: Reg["A"], 5: Reg["B"], 6: Reg["C"], 7: None}

    result = combo_operands[coperand] % 8
    Reg["B"] = result
    instruction_pointer += 2

def opcode3_jnz(lit_operand):
    global instruction_pointer
    global Reg
    combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: Reg["A"], 5: Reg["B"], 6: Reg["C"], 7: None}

    if Reg["A"] != 0:
        instruction_pointer = lit_operand
    else:
        instruction_pointer += 2

def opcode4_bxc(operand):
    global instruction_pointer
    global Reg
    combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: Reg["A"], 5: Reg["B"], 6: Reg["C"], 7: None}

    result = Reg["B"] ^ Reg["C"]
    Reg["B"] = result
    instruction_pointer += 2

def opcode5_out(coperand):
    combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: Reg["A"], 5: Reg["B"], 6: Reg["C"], 7: None}
    global instruction_pointer

    result = combo_operands[coperand] % 8
    instruction_pointer += 2
    return result

def opcode6_bdv(coperand):
    global instruction_pointer
    global Reg
    combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: Reg["A"], 5: Reg["B"], 6: Reg["C"], 7: None}

    result = int(Reg["A"] / (pow(2, combo_operands[coperand])))
    Reg["B"] = result
    instruction_pointer += 2

def opcode7_cdv(coperand):
    global instruction_pointer
    global Reg
    combo_operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: Reg["A"], 5: Reg["B"], 6: Reg["C"], 7: None}

    result = int(Reg["A"] / (pow(2, combo_operands[coperand])))
    Reg["C"] = result
    instruction_pointer += 2

output = ""
while instruction_pointer < len(Program):

    nextopcode = Program[instruction_pointer]
    nextoperand = Program[instruction_pointer + 1]

    if nextopcode == 0: opcode0_adv(nextoperand)
    elif nextopcode == 1: opcode1_bxl(nextoperand)
    elif nextopcode == 2: opcode2_bst(nextoperand)
    elif nextopcode == 3: opcode3_jnz(nextoperand)
    elif nextopcode == 4: opcode4_bxc(nextoperand)
    elif nextopcode == 5:
        output += str(opcode5_out(nextoperand)) + ","
    elif nextopcode == 6: opcode6_bdv(nextoperand)
    elif nextopcode == 7: opcode7_cdv(nextoperand)

print("P1Solution: " + str(output[:-1]))
finstring = (",").join(list(map(str, Program)))

movement = 1
StringToFind = finstring[len(finstring) - movement:len(finstring)]

bitends = ["000", "001", "010", "011", "100", "101", "110", "111"]
checkbits = ["000", "001", "010", "011", "100", "101", "110", "111"]

P2SolBits = []
StopTheCount = False

while movement <= 31:

    Reg = {"A": None, "B": None, "C": None}
    nextbits = []
    for checkbit in checkbits:
        Reg["A"] = int(checkbit, 2)
        Reg["B"] = 0
        Reg["C"] = 0
        instruction_pointer = 0
        output = ""

        while instruction_pointer < len(Program):

            nextopcode = Program[instruction_pointer]
            nextoperand = Program[instruction_pointer + 1]

            if nextopcode == 0: opcode0_adv(nextoperand)
            elif nextopcode == 1: opcode1_bxl(nextoperand)
            elif nextopcode == 2: opcode2_bst(nextoperand)
            elif nextopcode == 3: opcode3_jnz(nextoperand)
            elif nextopcode == 4: opcode4_bxc(nextoperand)
            elif nextopcode == 5:
                output += str(opcode5_out(nextoperand)) + ","
            elif nextopcode == 6: opcode6_bdv(nextoperand)
            elif nextopcode == 7: opcode7_cdv(nextoperand)

        if output[:-1] == StringToFind:
            nextbits.append(checkbit)

        if output[:-1] == finstring:
            P2SolBits.append(checkbit)
            StopTheCount = True

    if StopTheCount == False:
        checkbits = []
        for nextbit in nextbits:
            for bitend in bitends:
                checkbits.append(nextbit + bitend)

    movement += 2
    StringToFind = finstring[len(finstring) - movement:len(finstring)]


print("P2Solution: " + str(int(P2SolBits[0], 2)))


        
