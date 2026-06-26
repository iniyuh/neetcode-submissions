"""
generate all substrings and while generating check if duplicate via set
    O(n^2) time and O(n) space

sliding window + hash set
    O(n) time and O(n) space
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        hs = set(s[0])
        l, r = 0, 1
        maxLength = 1

        while r < len(s):
            if s[r] not in hs:
                hs.add(s[r])
                r += 1
                maxLength = max(maxLength, r - l)
            else:
                while s[l] != s[r]:
                    hs.remove(s[l])
                    l += 1
                hs.remove(s[l])
                l += 1
        
        return maxLength
                