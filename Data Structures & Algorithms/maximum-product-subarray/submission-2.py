class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        localMax = nums[0]
        actual = nums[0]

        for num in nums[1:]:
            actual *= num
            localMax = max(localMax, actual, num)

        nums.reverse()

        localMax2 = nums[0]
        actual2 = nums[0]

        for num in nums[1:]:
            actual2 *= num
            localMax2 = max(localMax2, actual2, num)


        return max(localMax, localMax2)
