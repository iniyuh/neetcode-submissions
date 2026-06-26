class Node:
    def __init__(self):
        self.hm = {}
        self.isWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.hm: node.hm[char] = Node()

            node = node.hm[char]
        
        node.isWord = True



    def search(self, word: str, node: Node = None) -> bool:
        if not node: node = self.root

        for i, char in enumerate(word):
            if char == '.':
                ret = False
                for n in node.hm.values():
                    ret |= self.search(word[i+1:], n)
                
                return ret
                
            elif char not in node.hm: return False

            node = node.hm[char]
        
        return node.isWord
        
