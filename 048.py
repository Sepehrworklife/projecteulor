# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:04:13 2022

@author: SajadRafati
"""
# projectEuler48 
# Self powers
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.
# output ==> 9110846700
j = 0
x = []

for i in range(1, 1001):
    j += 1
    i = i ** j
    x.append(i)
    z = sum(x)

print(str(z)[-10:]) # 9110846700