class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        
        maxLen = 0
        maxStr = (-1, -1)

        for i in range(len(s) - 1):
            l, r = i, i

            while -1 < l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    maxStr = (l, r)
                l -= 1
                r += 1
            
            l, r = i, i + 1

            while -1 < l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    maxLen = r - l + 1
                    maxStr = (l, r)
                l -= 1
                r += 1
        
        return s[maxStr[0]:maxStr[1] + 1]
