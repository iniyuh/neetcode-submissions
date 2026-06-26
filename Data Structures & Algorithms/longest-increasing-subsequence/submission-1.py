class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        hm = {}
        globalMax = 0

        def helper(i, prev=None):
            if prev and nums[i] <= prev: return 0
            elif i in hm: return hm[i]
            else:
                max_ = 0

                for j in range(i+1, len(nums)):
                    max_ = max(max_, helper(j, nums[i]))

                hm[i] = 1 + max_
                return hm[i]
        
        for i in range(len(nums)):
            globalMax = max(globalMax, helper(i))
        
        return globalMax