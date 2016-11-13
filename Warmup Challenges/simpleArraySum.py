#!/bin/python3

import sys


n = int(input())
numbers = input().split(' ')
summ = 0
for num in numbers:
    summ += int(num)

print(summ)