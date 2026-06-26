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
            if char in currNode.hm: currNode = currNode.hm[char]
            else:
                currNode.hm[char] = TrieNode()
                currNode = currNode.hm[char]
        
        currNode.isWord = True

    def search(self, word: str, currNode=None) -> bool:
        if not currNode: currNode = self.root

        if word == '.':
            for node in currNode.hm.values():
                if node.isWord: return True
            return False

        for i, char in enumerate(word):
            if char != '.' and char not in currNode.hm: return False
            elif char == '.':
                for node in currNode.hm.values():
                    if self.search(word[i+1:], node): return True
                return False
            else:
                currNode = currNode.hm[char]

        return currNode.isWord

            
