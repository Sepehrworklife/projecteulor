# -*- coding: utf-8 -*-
"""
Created on Sun Jul  3 00:04:13 2022

@author: Sajad
"""

# projecteuler 4
# Largest palindrome product 
# answer is 906609
x = []
y = []
z = []

for i in range(100, 1000):
    for j in range(100, 1000):
        a = i * j
        s = str(a)
        x.extend(s)
        y = x.copy()
        x.reverse()
        if x == y:
            z.append(a)
        x.clear()
        y.clear()

# answer should be 906609
print("Largest palindrome product is:", max(z)) 


"""
How to find out if the entered number or text is a palindrome
"""
j = str(input("Enter number or string: "))
n = j[::-1]
if j == n:
    print("This is palindrome: ", n)
else:
    print("This is not palindrome: ", n)