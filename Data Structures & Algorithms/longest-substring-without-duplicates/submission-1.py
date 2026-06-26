class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        maxLength = 0
        hashmap = {}

        while r < len(s):
            if s[r] in hashmap: 
                pivotIdx = hashmap[s[r]]

                for i in range(l, pivotIdx + 1):
                    del hashmap[s[i]]
                
                l = pivotIdx + 1

            hashmap[s[r]] = r
            maxLength = max(maxLength, r - l + 1)
            r += 1
        
        return maxLength

