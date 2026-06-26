class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def func(i, j):
            if i == len(text1) or j == len(text2): return 0
            if (i, j) in memo: return memo[i, j]

            if text1[i] == text2[j]: 
                memo[(i, j)] = 1 + func(i+1, j+1)
            else:
                memo[(i, j)] = max(func(i+1, j), func(i, j+1))
            return memo[(i, j)]
        
        return func(0, 0)