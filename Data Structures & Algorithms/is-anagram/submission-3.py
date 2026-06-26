class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        bucket1, bucket2 = [0] * 26, [0] * 26

        for i in range(len(s)):
            bucket1[ord(s[i]) - ord('a')] += 1 
            bucket2[ord(t[i]) - ord('a')] += 1 
        
        for i in range(26):
            if bucket1[i] != bucket2[i]: return False
        
        return True