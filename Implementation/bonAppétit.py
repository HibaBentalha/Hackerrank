#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(cost_temp) for cost_temp in input().strip().split(' ')]
b_charged = input().strip()
b_charged = int(b_charged)

shared = 0
b_actual = 0

for cost in c:
    shared += cost
    
shared = shared - c[k]
b_actual = shared / 2

if ((b_charged - int(b_actual)) == 0):
    print('Bon Appetit')
else:
    print(b_charged - int(b_actual))
    