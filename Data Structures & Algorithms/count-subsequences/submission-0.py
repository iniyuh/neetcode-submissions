class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def dfs(i, j):
            print(i, j)
            if j == len(t): 
                return 1
            elif i == len(s): return 0
            elif (i, j) in memo: return memo[(i, j)]

            ret = dfs(i+1, j)
            if s[i] == t[j]: 
                print('hit', i, j)
                ret += dfs(i+1, j+1)

            memo[(i, j)] = ret
            return memo[(i, j)]
        
        return dfs(0, 0)
