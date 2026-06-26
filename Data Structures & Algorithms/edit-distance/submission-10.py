class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2): word1, word2 = word2, word1
        L1, L2 = len(word1), len(word2)

        curr = [0] * (L1 + 1)
        prev = [L1 - i for i in range(L1 + 1)]
        p = []

        for j in range(L2 - 1, -1, -1):
            p.append(prev)
            curr[L1] = L2 - j

            for i in range(L1 - 1, -1, -1):
                if word1[i] == word2[j]: curr[i] = prev[i+1]
                else:
                    curr[i] = 1 + min(prev[i+1], curr[i+1], prev[i])
            
            prev = curr[:]
        p.append(prev)
        for arr in reversed(p):
            print(arr)
        
        return prev[0]
