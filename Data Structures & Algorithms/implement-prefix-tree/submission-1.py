class TrieNode:

    def __init__(self):
        self.hm = {}
        self.isWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currNode = self.root
        for char in word:
            if char in currNode.hm: currNode = currNode.hm[char]
            else: 
                currNode.hm[char] = TrieNode()
                currNode = currNode.hm[char]
        currNode.isWord = True

    def search(self, word: str) -> bool:
        currNode = self.root
        for char in word:
            if char in currNode.hm: currNode = currNode.hm[char]
            else: return False
        return currNode.isWord

    def startsWith(self, prefix: str) -> bool:
        currNode = self.root
        for char in prefix:
            if char in currNode.hm: currNode = currNode.hm[char]
            else: return False
        return True
        
        