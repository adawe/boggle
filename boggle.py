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

fill_table(table)
print_table(table)

dict_file = open("dict.txt")

words = [line.strip() for line in dict_file.readlines()]
trie = Trie()
for word in words:
    trie.add_word(word)


