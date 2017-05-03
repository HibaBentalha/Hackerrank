#!/bin/python3

import sys

def getRecord(s):
    highest_break_count = lowest_break_count = 0
    max_record = min_record = s[0] 
    for i in range(1, n):
        if (s[i] > max_record):
            max_record = s[i]
            highest_break_count += 1        
        elif (s[i] < min_record):
            min_record = s[i]
            lowest_break_count += 1       
    return highest_break_count, lowest_break_count

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))

result = getRecord(s)
print (" ".join(map(str, result)))