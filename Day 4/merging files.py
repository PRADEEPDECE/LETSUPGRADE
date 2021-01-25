# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:33:06 2021

@author: LENOVO
"""
data = data2 = "" 
  
# Reading data from file1 
with open('file1.txt') as fp: 
    data = fp.read() 
  
# Reading data from file2 
with open('file2.txt') as fp: 
    data2 = fp.read() 
  
# Merging 2 files 
 
data += "\n"
data += data2 
  
with open ('file3.txt', 'w') as fp: 
    fp.write(data) 

