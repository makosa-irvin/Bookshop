# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:16:22 2019

@author: User
"""
import csv
#function to open the csv
def load_books(filename):
    #define a list to contain the books
    bookshelf = []
    with open(filename) as file:
        #reads the csv
        shelf = csv.DictReader(file)
        #to remove punctuations
        
        #to select each book and lowercase them
        for book in shelf:
            
            
            book['title_lower']= book['title'].lower()
            book['author_lower']= book['author'].lower()
            
            
            bookshelf.append(book)
            
    return bookshelf