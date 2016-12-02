#!/bin/python3

import sys

n = int(input().strip())
numbers = input().strip().split(' ')

summ = 0
#range(n) = [0, 1, 2 ... n-1]
for i in range(n):
    summ += int(numbers[i])
    
#for num in numbers:
#   summ += int(num)
    
print(summ)

#arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]