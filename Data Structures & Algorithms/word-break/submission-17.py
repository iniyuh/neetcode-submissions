class Node:
    def __init__(self):
        self.hm = {}
        self.isWord = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Set up trie 
        root = Node()

        for word in wordDict:
            node = root

            for char in word:
                if char not in node.hm: node.hm[char] = Node()
                node = node.hm[char]

            node.isWord = True

        memo = {}
        
        def dfs(idx):
            if idx == len(s): return True
            elif idx in memo: return memo[idx]
            else:
                node = root
                i = idx 

                while i < len(s):
                    char = s[i]

                    if char not in node.hm: 
                        memo[idx] = False
                        return False
                    else: 
                        node = node.hm[char]
                        i += 1

                        if node.isWord and dfs(i): 
                            memo[idx] = False
                            return True
                
                memo[idx] = False
                return False
        
        return dfs(0)
                        
        

