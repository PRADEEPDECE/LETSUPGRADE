# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:31:34 2021

@author: LENOVO
"""


# initializing string  
input_str = "Python is good and Letsupgrade is also good"
# using set   
output = {x : input_str.count(x) for x in set(input_str )}  
  
# printing result  
print ("Occurrence of all characters in GeeksforGeeks is :\n "+ str(output)) 