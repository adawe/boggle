
class Trie(dict):

    def __init__(self, parent=None):

        self.parent = parent
        self.marker = None

    def insert(self, word):

        if not word:
            return
        if word[0] not in self:
            self[word[0]] = ((len(word) == 1), Trie(parent=self))
        self[word[0]][1].insert(word[1:])
    
    def __contains__(self, chars):

        if len(chars) == 0:
            return False
        elif len(chars) == 1:
            return super(Trie, self).__contains__(chars)
        return (chars[0] in self) and (chars[1:] in self[chars[0]][1])

    def isword(self, chars):

        if len(chars) == 0:
            return False
        if len(chars) == 1:
            return (chars in self) and self[chars][0]
        return (chars[0] in self) and self[chars[0]][1].isword(chars[1:])
    
    def down(self, char):

        if char in self:
            self.marker = char
            return self[char]
        return False, None
    
    def up(self):
    
        self.marker = None
        return self.parent     
