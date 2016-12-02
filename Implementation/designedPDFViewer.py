#!/bin/python3

import sys


h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()

# heights = dict()
# letters = "abcdefghijklmnopqrstuvwxyz"
#h= [1, 3, 1, 3, 1, ... 5]
# for i in range(26):
   #heights['a'] = h[0]
   #heights['b'] = h[1]
    # heights[letters[i]] = h[i]


maxi = 0
for letter in word:
    if(h[ord(letter)-97] > maxi):
        maxi = h[ord(letter)-97]

print(len(word)*maxi)