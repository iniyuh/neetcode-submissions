class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        ret = float('-inf')

        for num in nums:
            s += num
            ret = max(ret, s)
            if s < 0: s = 0
        
        return ret
