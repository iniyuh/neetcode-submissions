class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        remainder = 0
        for num in nums:
            remainder ^= num
        return remainder
