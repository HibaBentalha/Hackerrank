#!/bin/python3

import sys


t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    height = 1
    i = 0 
    while (i < n):
        height = height * 2
        i += 1
        if (i < n):
            height += 1
        i += 1
    print(height)  