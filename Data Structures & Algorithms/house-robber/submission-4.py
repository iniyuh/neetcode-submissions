class Solution:
    def rob(self, nums: List[int]) -> int:
        hm = {}

        def helper(i):
            if i in hm: return hm[i]
            elif i == len(nums) - 1: 
                hm[i] = nums[i]
                return hm[i]
            elif i == len(nums) - 2: 
                hm[i] = max(nums[i], nums[i + 1])
                return hm[i]
            else:
                hm[i] = max(nums[i] + helper(i + 2), helper(i + 1))
                print(i, hm[i])
                return hm[i]
        
        helper(0)
        return hm[0]