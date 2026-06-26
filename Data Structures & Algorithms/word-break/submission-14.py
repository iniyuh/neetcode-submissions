class TrieNode:
    def __init__(self):
        self.hm = {}
        self.isWord = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        memo = set()

        for word in wordDict:
            node = root
            for char in word:
                if char not in node.hm: node.hm[char] = TrieNode()
                node = node.hm[char]
            node.isWord = True

        def helper(l):
            if l == len(s): return True
            elif l in memo: return False

            node = root
            callStack = []

            L = l

            while l < len(s) and s[l] in node.hm:
                node = node.hm[s[l]]
                
                if node.isWord: 
                    callStack.append(l+1)
                
                l += 1
            
            for i in reversed(callStack): 
                if helper(i): return True
            
            memo.add(L)
            return False
        
        return helper(0)
        