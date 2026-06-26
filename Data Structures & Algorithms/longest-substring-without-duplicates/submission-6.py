"""
Brute force:
    Generate every substring O(n^2) time O(n) space
    Validate every string for duplicates O(n) time and O(n) space for the set
    Overall O(n^3) time and O(n) space
Sliding window:
    Use a set to keep track of characters present in window O(n) space
    Iterate l and r pointers through entire string maintaining a window without dupes O(n) time and O(1) space
    Keep track of the maximum valid window size O(1) space
    Overall O(n) time and O(n) space

    While r < len(s)
    While char is in set: set.remove(left char)
    l, r start at 0, 0
    we add character at r position
    imply l <= r in code

Examples:
    _ = 0
    1 2 3 4 5 = 5
    1 2 1 3 4 = 4
    2 1 1 3 4 = 3
    1 2 3 4 1 = 4
    1 2 3 4 4 5 6 7 8 = 5
    1 2 3 4 1 5 6 = 6
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        l, r = 0, 0
        maxLength = 0

        while r < len(s):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            
            hs.add(s[r])
            maxLength = max(maxLength, r - l + 1)

            r += 1
        
        return maxLength


