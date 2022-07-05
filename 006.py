# -*- coding: utf-8 -*-
"""
Created on sun Jul  6 00:04:13 2022

@author: SajadRafati
"""
# projecteuler 6
# Sum square difference
"""
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
# answer is: "25164150"
x = []
y = []
for i in range(1, 101):
    i **= 2
    x.append(i)
    z = sum(x)
    b = int(z)
for j in range(1, 101):
    y.append(j)
    v = sum(y)
    v **= 2 
    
print(v - b)