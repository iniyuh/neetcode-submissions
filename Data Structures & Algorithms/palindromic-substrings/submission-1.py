class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 0: return 0

        counter = 1

        for i in range(len(s) - 1):
            l1, r1 = i, i

            while l1 != -1 and r1 != len(s) and s[l1] == s[r1]: 
                counter += 1
                l1 -= 1
                r1 += 1

            l2, r2 = i, i + 1
            while l2 != -1 and r2 != len(s) and s[l2] == s[r2]: 
                counter += 1
                l2 -= 1
                r2 += 1
        
        return counter