#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apples = [int(apple_temp) for apple_temp in input().strip().split(' ')]
oranges = [int(orange_temp) for orange_temp in input().strip().split(' ')]

#Calculate the apples positions
apples_in = 0
for apple in apples:
    distance = a + apple
    if (distance <= t and distance >= s):
        apples_in += 1
print(apples_in)


#Calculate the oranges positions 
oranges_in = 0
for orange in oranges:
    distance = b + orange
    if (distance <= t and distance >= s):
        oranges_in += 1
print(oranges_in)

