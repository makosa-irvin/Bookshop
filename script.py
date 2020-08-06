# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 11:29:03 2019

@author: User
"""

import reader
import sorts
import searchbook
#to read the csv

long_bookshelf = reader.load_books('largebook.csv')
long_bookshelf_v2=long_bookshelf.copy()
long_bookshelf_v1=long_bookshelf.copy()
#the compare functions
def by_title_ascending(book_a,book_b):
    if book_a['title_lower']>book_b['title_lower']:
        return True
    else:
        return False
    
def by_author_ascending(book_a,book_b):
    if book_a['author_lower']>book_b['author_lower']:
        return True
    else:
        return False
    
def by_total_length(book_a,book_b):
    return (len(book_a['title_lower'])+len(book_a['author_lower']))>(len(book_b['title_lower'])+len(book_b['author_lower']))
#sorting the books using bubblesort  

    
    
#sorting the large books
#by title
sorts.quicksort(long_bookshelf_v1,0,len(long_bookshelf_v1)-1,by_title_ascending)
#by author
sorts.quicksort(long_bookshelf_v2,0,len(long_bookshelf_v2)-1,by_author_ascending)
#by total length of title and author
#sorts.quicksort(long_bookshelf_v1,0,len(long_bookshelf_v1)-1,by_total_length)
#sort3 = sorts.bubble_sort(long_bookshelf_v1,by_total_length)
long_titles = []
long_authors = []
for book in long_bookshelf_v1:
    #by title
    #print(book['title_lower'],'\n')
   
    #by total length of title and author
    #print((len(book['title_lower'])+len(book['author_lower'])))
    
    long_titles.append(book['title_lower'])

#print(long_titles)
#print(long_authors)
for book in long_bookshelf_v2:
    #by author
    #print(book['author_lower'],'\n')
    long_authors.append(book['author_lower'])
    
searched_book = input("Enter book title or author: ")
searched_book = searched_book.lower()
#punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    
#checking if searched book in library
search2 = searchbook.binary_search_book(long_titles,searched_book,0,len(long_titles))
search3 = searchbook.binary_search_book(long_authors,searched_book,0,len(long_authors))
if search2 == True:
    print("The {0} book  is found at index {1}".format(searched_book,long_titles.index(searched_book)))
    print("sorted by title")
elif search3 == True:
    
    print("The {0} books are found starting at index {1}".format(searched_book,long_authors.index(searched_book)))
    print("sorted by author")
else :
    print('{0} is not in library'.format(searched_book))

