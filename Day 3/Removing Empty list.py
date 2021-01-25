# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:20:45 2021

@author: LENOVO
"""


init_list = [9, 8, [], 6, [], [], 3] 
  
 
print("The init list is : " + str(init_list)) 
  
#removing empty list
result = [ele for ele in init_list if ele != []] 
  
# printing result  
print ("List after empty list removal : " + str(result)) 