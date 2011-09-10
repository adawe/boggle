#!/usr/bin/env python

import string
import random
from trie import Trie
from copy import copy

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

def recursive_traverse(table, col, row, trie, word="", visited=None):
    
    words = []
    if col < 0 or col >= len(table) \
       or row < 0 or row >= len(table[0]):
        return words
    if visited is None:
        visited = []
    if (col, row) not in visited:
        visited.append((col, row))
    else:
        return words

    if table[col][row] in trie:
        word += table[col][row]
    else:
        return words
    isword, subtrie = trie[table[col][row]]
    if isword:
        words.append(word)
    if subtrie is not None:
        # try up
        words += recursive_traverse(table, col, row-1, subtrie, word, copy(visited))
        # up right
        words += recursive_traverse(table, col+1, row-1, subtrie, word, copy(visited))
        # try right
        words += recursive_traverse(table, col+1, row, subtrie, word, copy(visited))
        # try down right
        words += recursive_traverse(table, col+1, row+1, subtrie, word, copy(visited))
        # try down
        words += recursive_traverse(table, col, row+1, subtrie, word, copy(visited))
        # try down left 
        words += recursive_traverse(table, col-1, row+1, subtrie, word, copy(visited))
        # try left
        words += recursive_traverse(table, col-1, row, subtrie, word, copy(visited))
        # try up left
        words += recursive_traverse(table, col-1, row-1, subtrie, word, copy(visited))
    return words

fill_table(table)
print_table(table)

dict_file = open("dict.txt")
words = [line.strip() for line in dict_file.readlines()]
dict_file.close()
trie = Trie()
map(trie.insert, words)

words = []
for col in range(len(table)):
    for row in range(len(table[0])):
        words += recursive_traverse(table, col, row, trie)

for word in words:
    print word
