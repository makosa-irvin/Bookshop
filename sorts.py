# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:36:57 2019

@author: User
"""
from random import randrange

def bubble_sort(arr,compare_function):
    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(arr)-1):
            if compare_function(arr[idx],arr[(idx + 1)]):
                sorted = False
                arr[idx],arr[(idx + 1)]=arr[(idx + 1)],arr[idx]
    return arr

def quicksort(list,start,end,compare_function):
    #base case if list has one or less elements
    if start >= end:
        return
    #randomising the pivot for efficiency
    pivot_idx = randrange(start,end+1)
    pivot_elem = list[pivot_idx]
    #placing pivot at the end of list 
    list[pivot_idx],list[end]=list[end],list[pivot_idx]
    #defining variable to place elements greater or less than 
    lesser_than_pointer = start
    #iterating through list
    for i in range(start,end):
        #comparing pivot and i
        if compare_function(pivot_elem,list[i]):
            #switching lesser_than_pointer with i
            list[i],list[lesser_than_pointer]=list[lesser_than_pointer],list[i]
            #incrementing lesser than pointer
            lesser_than_pointer += 1
            
    #switching lesser than_pointer with pivot which is at the end
    list[lesser_than_pointer],list[end]=list[end],list[lesser_than_pointer]
    
    #recursive call the greater and lesser list
    quicksort(list,start,(lesser_than_pointer-1),compare_function)
    quicksort(list,(lesser_than_pointer+1),end,compare_function)
    return list
    
    
    