# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:25:40 2021

@author: LENOVO
"""


string = "Python is good and Letsupgrade is also good"
c = string.split() 
data = [] 
for i in c: 
  
    # If condition is used to store unique string  
    # in another list 'k'  
    if (string.count(i)>1 and (i not in data)or string.count(i)==1): 
        data.append(i) 
print(' '.join(data))