class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i, num in reversed(list(enumerate(nums))):
            if i + num >= goal: 
                goal = i

        return goal == 0
