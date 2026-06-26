"""
Brute force, find every subarray O(n^2) then compute product and update max O(n)
    = O(n^3) time
    = O(1) space using pointers


"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = 1
        ret = nums[0]

        for num in nums:
            temp = num * curMax
            curMax = max(temp, num * curMin, num)
            curMin = min(temp, num * curMin, num)
            ret = max(ret, curMax)
            print(curMax, curMin, ret)
        
        return ret
