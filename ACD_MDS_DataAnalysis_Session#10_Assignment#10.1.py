# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 08:43:37 2018

@author: HP
"""

# Program/function to compute moving average
def mov_avg(inp_arr,n):
    leninp = len(inp_arr)
    iterval = leninp - n + 1
    for i in range(iterval):
        sum = 0
        avg = 0
        for j in range (i, i+n):
            sum = sum + inp_arr[j]
        avg = sum/n
        print(avg)
#   end of function        
test_arr = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
mov_avg(test_arr,3)