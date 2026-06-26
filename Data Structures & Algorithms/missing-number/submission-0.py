class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def summation(i):
            if i == 0: return 0
            return i + summation(i-1)
        
        total = summation(len(nums))
        actual = sum(nums)
        return total - actual