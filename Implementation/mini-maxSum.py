#!/bin/python

import sys

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]
new_tab = [a,b,c,d,e]
new_tab = sorted(new_tab)

mini = 0
maxi = 0
for i in range(4):
    mini += new_tab[i]
    
for j in range(1,5):
    maxi += new_tab[j]

print(mini, maxi)
