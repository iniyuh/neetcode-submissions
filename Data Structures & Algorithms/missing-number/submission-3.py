class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return sum([i for i in range(len(nums) + 1)]) - sum(nums)

        n = len(nums)

        ret = 0
        i = 0
        while i < n:
            ret += i
            ret -= nums[i]

            i += 1
        
        ret += n
        return ret