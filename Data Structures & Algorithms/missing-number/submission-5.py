class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sumOfNums = 0
        sumOfRange = 0

        for i, num in enumerate(nums): 
            sumOfNums += num
            sumOfRange += i
        
        sumOfRange += len(nums)

        return sumOfRange - sumOfNums
