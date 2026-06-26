"""
Brute force: iterate through whole thing, first time an element is smaller than the 
    previous, that's our min, if we never find that condition the first element is the 
    min, O(n) time and O(1) space

Modified binary search: binary search modified in the following ways:
    - if l < m and m > r then we know target is to the right of m
    - if l > m and m < r then we know that target is to the left of or is m

"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]: return nums[0]

        l, r = 0, len(nums)

        while l < r:
            m = (l + r) // 2

            if nums[l] < nums[m]: l = m 
            else: 
                if nums[m-1] > nums[m]: return nums[m]
                else: r = m
        
        return nums[l - 1]