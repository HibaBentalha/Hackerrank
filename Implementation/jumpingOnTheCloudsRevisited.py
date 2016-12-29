#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
E = 100

for i in range(n):
    if(i % k == 0):
        if(c[i] == 1):
            E -= 3
        else:
            E -= 1
print(E)
    