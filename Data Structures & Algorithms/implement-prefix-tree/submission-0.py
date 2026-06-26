class Node:
    def __init__(self, val, hashmap=None):
        self.val = val
        self.hashmap = hashmap if hashmap is not None else {}

class PrefixTree:

    def __init__(self):
        self.hashmap = {}

    def insert(self, word: str) -> None:
        i = 0
        curMap = self.hashmap

        while i < len(word) and word[i] in curMap:
            curMap = curMap[word[i]].hashmap
            i += 1
        
        while i < len(word):
            curMap[word[i]] = Node(word[i])
            curMap = curMap[word[i]].hashmap
            i += 1
        
        curMap["END"] = True


    def search(self, word: str) -> bool:
        curMap = self.hashmap

        for char in word:
            if char not in curMap: return False
            else:
                curMap = curMap[char].hashmap
        
        return "END" in curMap

    def startsWith(self, prefix: str) -> bool:
        curMap = self.hashmap

        for char in prefix:
            if char not in curMap: return False
            else:
                curMap = curMap[char].hashmap
        
        return True
        
        