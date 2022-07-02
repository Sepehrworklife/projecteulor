# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 00:40:20 2022

@author: Sajad
"""

# projecteuler 2
# Even Fibonaccci numbers
first_number = 1
second_number = 1
Sum = 0

while first_number < 4000000:
    if first_number % 2 == 0:
        Sum += first_number
    new = first_number + second_number
    first_number = second_number
    second_number = new
    
print("sum number is: ", Sum)
