
class Trie(dict):

    def add_word(self, word):

        self.__recurse_add_word(word)

    def __recurse_add_word(word, subtree=self):

        if not word:
            return
        if word[0] not in subtree:
            subtree[word[0]] = {}
        self.__recurse_add_word(word[1:], subtree[word[0]])
