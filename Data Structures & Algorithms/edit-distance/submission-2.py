class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # for each character:
            # if match, increment both pointers
            # otherwise
                # if remainder w1 < remainder w2 try inserting
                # if remainder w1 > remainder w2 try deleting
                # try replacing
        memo = {}

        def helper(i, j):
            if j == len(word2): return len(word1) - i
            elif i == len(word1): return len(word2) - j
            elif (i, j) in memo: return memo[(i, j)]
            elif word1[i] == word2[j]: 
                memo[(i, j)] = helper(i+1, j+1)
                return memo[(i, j)]
            else:
                memo[(i, j)] = helper(i+1, j+1) + 1
                # if len(word1) - i < len(word2) - j: 
                memo[(i, j)] = min(memo[(i, j)], helper(i, j+1) + 1)
                # if len(word2) - j < len(word1) - i: 
                memo[(i, j)] = min(memo[(i, j)], helper(i+1, j) + 1)

                return memo[(i, j)]
        
        return helper(0, 0)

