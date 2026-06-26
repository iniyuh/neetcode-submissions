class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = set()

        def helper(i):
            if i == len(nums) - 1: return True
            elif i >= len(nums) or i in memo: return False
            else:
                for j in range(nums[i], 0, -1):
                    if helper(i + j): return True
                
                memo.add(i)
                return False
        
        return helper(0)