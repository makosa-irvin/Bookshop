# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:00:00 2019

@author: User
"""

def binary_search_book(data,target,low,high):
    
    if low>=high:
        #print(matches)
        return False
    else:
        mid = (low+high)//2
        
        if data[mid]==target:
            
            
            return True
        else:
            if data[mid]>target:
                return binary_search_book(data,target,low,mid)
            if data[mid]<target:
                return binary_search_book(data,target,mid+1,high)
    
    
def linear_search_book(data,target):
    for booky in data:
        if booky == target:
            print('i have found it')
            break
    else:
        print('not in the library')
    