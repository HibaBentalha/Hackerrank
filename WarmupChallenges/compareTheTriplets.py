#!/bin/python3

import sys


A = input().strip().split(' ') 
B = input().strip().split(' ')

scoreA = 0
scoreB = 0
for i in range(3):
    if int(A[i]) < int(B[i]):
        scoreB += 1
    elif int(A[i]) > int(B[i]):
        scoreA += 1
        
print(scoreA, scoreB)