# -*- coding: utf-8 -*-
"""
Created on Sat Jul  2 00:06:16 2022

@author: Sajad
"""

# project number1 euler
# Multiples of 3 or 5
def divisible_numbers():
    divisible_number = 0
    
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            divisible_number += num  
        
    print("total number of 3 or 5 is: ", divisible_number)

divisible_numbers()