# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:42:29 2021

@author: LENOVO
"""


# Python program to calculate the sum of n  Numbers
#n is number of values
num = int(input("Enter the value of n: "))
n = num
sum = 0

if num <= 0: 
   print("Enter a whole positive number!") 
else: 
   while num > 0:
        sum = sum + num
        num = num - 1; 
    
   print("Sum of first", n, " numbers is: ", sum)