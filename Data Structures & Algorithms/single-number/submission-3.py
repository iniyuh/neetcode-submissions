class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ret = nums[0]

        for num in nums[1:]:
            ret = ~(ret ^ num)
        
        return ret