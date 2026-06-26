class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1: return s
        
        maxLen = 0
        maxStr = ''

        for i in range(len(s) - 1):
            l1, r1 = i, i
            while r1 != len(s) and l1 != -1 and s[l1] == s[r1]:

                if r1 - l1 + 1 > maxLen:
                    maxLen = r1 - l1 + 1
                    maxStr = s[l1:r1+1]

                l1 -= 1
                r1 += 1
                # print(l1, r1)

                
            
            l2, r2 = i, i + 1
            while l2 != -1 and r2 != len(s) and s[l2] == s[r2]:
                if r2 - l2 + 1 > maxLen:
                    print(r2, l2)
                    maxLen = r2 - l2 + 1
                    maxStr = s[l2:r2+1]

                l2 -= 1
                r2 += 1

                
        
        return maxStr
