class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 1

        for i in range(len(s) - 1):
            l, r = i, i

            while -1 < l and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
            l, r = i, i+1

            while -1 < l and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            
        return count