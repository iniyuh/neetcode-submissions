class Node:
    def __init__(self, isWord=False):
        self.hm = {}
        self.isWord = isWord

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        
        for char in word:
            if char not in node.hm: node.hm[char] = Node()

            node = node.hm[char]
        
        node.isWord = True

    def search(self, word: str, node=None) -> bool:
        if not node: node = self.root

        for i, char in enumerate(word):
            if char != '.':
                if char not in node.hm: return False
                else:
                    node = node.hm[char]
            else:
                res = False
                for n in node.hm.values():
                    res |= self.search(word[i+1:], n)
                return res
        
        return node.isWord
