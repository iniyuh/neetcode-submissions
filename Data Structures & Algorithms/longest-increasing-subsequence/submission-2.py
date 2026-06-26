class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        def dfs(prev, i):
            if i == len(nums): return 0
            elif nums[i] <= prev: return dfs(prev, i + 1)
            else:
                return max(
                    1 + dfs(nums[i], i + 1), 
                    dfs(prev, i + 1)
                )
        
        # case where no increasing subsequence
        return dfs(float('-inf'), 0)
        

