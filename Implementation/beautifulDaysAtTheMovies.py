#!/bin/python3

import sys

def reversed_string(a_string):
    return int(a_string[::-1]);

i,j,k = input().strip().split(' ')
i,j,k = [int(i),int(j),int(k)]
c = 0
for x in range(i,j+1):
    if(x - reversed_string(x) % k == 0):
        c = +1
print(c)