class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hm = {}
        max_ = 0

        for num in nums:
            hm[num] = hm.get(num - 1, 0) + 1

            i = num + 1
            curr = hm[num]
            while i in hm:
                hm[i] = curr + 1
                curr += 1
                i += 1

            max_ = max(max_, hm[i - 1])
        
        return max_
        
