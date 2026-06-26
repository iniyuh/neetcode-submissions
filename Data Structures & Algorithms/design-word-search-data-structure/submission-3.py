class TrieNode:
    def __init__(self):
        self.hm = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        currNode = self.root

        for char in word:
            if char not in currNode.hm: currNode.hm[char] = TrieNode()

            currNode = currNode.hm[char]
        
        currNode.isWord = True

    def search(self, word: str, currNode=None) -> bool:
        if currNode is None: currNode = self.root

        for i, char in enumerate(word):
            if char == '.':
                for letter in currNode.hm.keys():
                    if self.search(letter + word[i+1:], currNode): return True
                return False
            elif char not in currNode.hm: return False
            else: currNode = currNode.hm[char]
        
        return currNode.isWord
        



