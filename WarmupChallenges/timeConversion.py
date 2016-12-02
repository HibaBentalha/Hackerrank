#!/bin/python3

import sys


time = input().strip()
am_pm = time[8]
elmts = time[:-2].split(":")

if (am_pm == 'A') and (elmts[0] == '12'):
    elmts[0] = '00'
elif (am_pm == 'P') and (elmts[0] != '12'):
    elmts[0] = str(int(elmts[0]) + 12)
print(':'.join(elmts)) 