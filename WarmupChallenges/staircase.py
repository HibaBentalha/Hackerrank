#!/bin/python3

import sys


n = int(input().strip())

k = n - 1
m = 1

while(m <= n):
    print(' ' * k + '#' * m)
    k -= 1
    m += 1
