#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
out = 0 

for i in range(n-1):
    for j in range(i+1,n):
        if(i < j):
            if( (a[i] + a[j]) % k == 0 ):
                out += 1
            
print(out)