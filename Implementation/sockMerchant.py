#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
socks = 0

for i in range(n-1):
    for j in range(i+1,n):
        if (c[i] == 0 and c[j] == 0):
            break
        if (c[i] == c[j]):
            c[i] = 0
            c[j] = 0           
            socks += 1
            break    
print(socks)