#!/usr/bin/env python

import string
import random
from trie import Trie

letters = string.letters[:26]

table_row = [None, None, None, None, None]
table = [table_row[:], table_row[:], table_row[:], table_row[:], table_row[:]]

def print_table(table):
    
    for row in table:
        print "".join(row)        
        
def fill_table(table):

    for row in table:
        for i in range(len(row)):
            row[i] = random.choice(letters)

def recursive_traverse(table, col, row, trie, word="", words=None, visited=None):
    
    if words is None:
        words = []
    if visited is None:
        visited = []
    if (col, row) not in visited:
        visited.append((col, row))
    else:
        return words
    # try up
    # try right
    # try down
    # try left
    return words

fill_table(table)
print_table(table)

dict_file = open("dict.txt")
words = [line.strip() for line in dict_file.readlines()]
dict_file.close()
trie = Trie()
map(trie.insert, words)

for word in words:
    print trie.isword(word)

words = []
for col in range(len(table)):
    for row in range(len(col)):
        words += recursive_traverse(table, col, row, trie)

for word in words:
    print word
