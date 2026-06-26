class Node:

    def __init__(self, isWord=False):
        self.hm = {}
        self.isWord = isWord


class PrefixTree:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.hm: node.hm[char] = Node()

            node = node.hm[char]
        
        node.isWord = True

    def search(self, word: str) -> bool:
        node = self.root
        
        for char in word:
            if char not in node.hm: return False
            else: node = node.hm[char]
        
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for char in prefix:
            if char not in node.hm: return False
            else: node = node.hm[char]
        
        return True
        
        