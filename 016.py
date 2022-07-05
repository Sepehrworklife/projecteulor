# -*- coding: utf-8 -*-
"""
Created on sun Jul  6 00:04:13 2022

@author: SajadRafati
"""

# projecteuler 16
# Power digit sum
# What is the sum of the digits of the number 2**1000?
# answer is: "1366"
x = []
for i in str(2 ** 1000):
    n = int(i)
    x.append(n)
print("sum of the digits of the number is: ",sum(x))