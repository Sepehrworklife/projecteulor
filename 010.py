# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:04:13 2022

@author: SajadRafati
"""
# projectEuler 10
# Summation of primes
# Find the sum of all the primes below two million.
def sum_prime():
    x = []
    for num in range(1, 2000000 + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                x.append(num)
                z = sum(x)
    print(z)
    
sum_prime()
