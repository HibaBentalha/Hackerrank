#!/bin/python3

import sys

def solve(grades):
    # Complete this function
    for i in range(n):
        if (grades[i] >= 38):
            next_multi_of5 = grades[i] + (5 - (grades[i] % 5))
            if (next_multi_of5 - grades[i] < 3):
                grades[i] = next_multi_of5
    return grades 

n = int(input().strip())
grades = []
grades_i = 0
for grades_i in range(n):
   grades_t = int(input().strip())
   grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))