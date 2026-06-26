class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0

        length = 0
        l, r = 0, 0
        record = set()

        while l <= r and r < len(s): 
            if s[r] not in record:
                record.add(s[r])
                length += 1
                maxLength = max(maxLength, length)

                r += 1
            else:
                while s[r] in record: 
                    record.remove(s[l])
                    l += 1
                    length -= 1
        
        return maxLength


