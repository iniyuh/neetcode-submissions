class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]

        cMin = nums[-1]
        l, r = 0, len(nums)
        m = 0

        while l < len(nums) and -1 < r and l != r:
            m = (r - l) // 2 + l
            if nums[m] > cMin:
                l = m + 1
            else:
                r = m 
                cMin = nums[m]
        
        return cMin

            