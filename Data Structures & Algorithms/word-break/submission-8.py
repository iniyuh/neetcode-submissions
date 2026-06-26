class Node:
    def __init__(self):
        self.hm = {}
        self.isWord = False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = Node()

        for word in wordDict:
            node = trie
            for char in word:
                if char not in node.hm: node.hm[char] = Node()
                node = node.hm[char]
            node.isWord = True


        stack = [0]
        visited = set()

        while stack:
            node = trie
            r = stack.pop()

            if r in visited: continue

            visited.add(r)

            while r < len(s):
                if s[r] not in node.hm: break

                node = node.hm[s[r]]
                if node.isWord: stack.append(r + 1)
                
                r += 1
            
            if r == len(s) and node.isWord: return True
        
        return False