# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 10:55:58 2021

@author: LENOVO
"""


# Python program to display all the prime numbers within an interval

start = int(input("Enter a starting number: ")) 
end = int(input("Enter a ending number: ")) 

print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)