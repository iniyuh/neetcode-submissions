class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visited = set()

        def helper(i):
            if i in visited: return False
            visited.add(i)

            for word in wordDict:
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    if i + len(word) == len(s): return True
                    elif helper(i + len(word)): return True
            
            return False
        
        return helper(0)
