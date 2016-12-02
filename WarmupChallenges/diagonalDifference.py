#!/bin/python3

import sys


n = int(input())
numbers = []
for i in range(n):
    numbers.append(input().strip().split(' '))
	#numbers[i] = input().strip().split(' ')

diag1 = 0
for i in range(n):
    diag1 += int(numbers[i][i])

diag2 = 0
for i in range(n):
    diag2 += int(numbers[i][n-1-i])

print(abs(diag1 - diag2)) 