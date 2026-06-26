class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2

            if target < nums[m]:
                r = m
            elif nums[m] < target: 
                l = m + 1
            else: return m
        
        return -1