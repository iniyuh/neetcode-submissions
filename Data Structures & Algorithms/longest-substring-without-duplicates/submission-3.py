class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        l = 0
        maxLength = 0

        for r, char in enumerate(s):
            if char not in hm or hm[char] < l: 
                hm[char] = r
            else:
                l = hm[char] + 1 
                hm[char] = r

            maxLength = max(maxLength, r - l + 1)
        
        return maxLength


            