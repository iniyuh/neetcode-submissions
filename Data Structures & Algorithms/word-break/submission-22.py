class TreeNode:
    def __init__(self):
        self.hm = {}
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()
    
    def add(self, word):
        currNode = self.root

        for char in word:
            if char not in currNode.hm: currNode.hm[char] = TreeNode()

            currNode = currNode.hm[char]
        
        currNode.isWord = True

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = PrefixTree()
        for word in wordDict:
            trie.add(word)

        memo = set()
        
        def dfs(i):
            if i in memo: return False
            print(i)
            if i == len(s): return True
            memo.add(i)

            candidateList = []
            currNode = trie.root

            while i < len(s) and s[i] in currNode.hm: 
                currNode = currNode.hm[s[i]]
                i += 1 

                if currNode.isWord:
                    candidateList.append(i)
            
            for candidate in reversed(candidateList):
                if dfs(candidate): return True
            
            return False
        
        return dfs(0)
            

        