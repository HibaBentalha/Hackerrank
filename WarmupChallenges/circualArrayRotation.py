#!/bin/python3

import sys

def rotate(tab, n):
    return tab[-n:] + tab[:-n]

def rotate_it(tab, n):
    l = len(tab)
    res = []
    for k in range(l - n, l):
        res.append(tab[k])
    for k in range(l - n):
        res.append(tab[k])
    return res

n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
a = rotate_it(a, k % n)
for a0 in range(q):
    m = int(input().strip())    
    print(a[m])