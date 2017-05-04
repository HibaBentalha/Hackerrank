#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

max_height = 0
number_of_candles = 0
for i in range(n):
    if(height[i] > max_height):
        max_height = height[i]
        number_of_candles = 1
    elif(height[i] == max_height):
        number_of_candles += 1
print(number_of_candles)