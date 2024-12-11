import re
import statistics
from copy import deepcopy
import numpy as np
import time
from functools import cache
from collections import defaultdict

# Since the normal way would be overkill we just make a dict where we have the results of each number already (to avoid doing it many many times)
# So we check: which numbers are new -> introduce them to tokens 
# And in newnums make +1, since we got that number one more time

data = ()
with open(r"C:\Users\Roko\Desktop\AoC 2024\24-AoC-D11.txt") as file:
    numbers = defaultdict(int)
    for line in file:
        data = tuple(map(int, line.rstrip().split(" ")))

for d in data:
    numbers[d] += 1

def blink(num):

    if num == 0:
        return (1,)
    
    elif len(str(num)) % 2 == 0:
        numstring = str(num)
        half = int(len(numstring)/2)
        return (int(numstring[:half]), int(numstring[half:]))
    
    else:
        return (num * 2024,)
    
tokens = {}

def step(nums):
    newnums = defaultdict(int)
    for n in nums:
        if n not in tokens:
            tokens[n] = blink(n)
        for k in tokens[n]:
            newnums[k] += nums[n]
    return newnums

# Solution (Just Change the range to 25 and 75 dependent on P1 or P2)
for i in range(0, 75):
    numbers = step(numbers)
    print(numbers)
print(sum([numbers[k] for k in numbers]))





