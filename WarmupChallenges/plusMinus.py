#!/bin/python3

import sys


n = int(input().strip())
numbers = input().strip().split(' ')
positive = 0
negative = 0
zeroes = 0

for i in range(n):
    if int(numbers[i]) > 0:
        positive += 1
    elif int(numbers[i]) < 0:
        negative += 1
    elif int(numbers[i]) == 0:
        zeroes +=1

print(int(positive)/n)
print(int(negative)/n)
print(int(zeroes)/n)
