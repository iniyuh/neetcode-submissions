"""
Notes:
If we imagine a tree, every time we reach a * there are three child paths
    However, say we are keeping track of unpaired brackets, if we have 0 
    lefts atm we know * = either ( or ""

Brute force: DFS where the tree is linear except for * nodes which have 3 
    subpaths time is O(3^n) and space is O(n)
Memoization: time is O(n^2) and space is O(n^2)

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}

        def dfs(i, unclosed):
            if i == len(s): return unclosed == 0

            if (i, unclosed) in memo: return memo[(i, unclosed)]

            memo[(i, unclosed)] = s[i] == '(' and dfs(i+1, unclosed + 1) or s[i] == ')' and unclosed > 0 and dfs(i+1, unclosed - 1) or s[i] == '*' and ( dfs(i+1, unclosed) or dfs(i+1, unclosed + 1) or (unclosed != 0 and dfs(i+1, unclosed - 1)) )

            return memo[(i, unclosed)]
        
        return dfs(0, 0)

