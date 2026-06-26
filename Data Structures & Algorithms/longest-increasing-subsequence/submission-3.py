class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}

        def dfs(prev, i):
            if i == len(nums): return 0
            elif (prev, i) in memo: return memo[(prev, i)]
            elif nums[i] <= prev: 
                memo[(prev, i)] = dfs(prev, i + 1)
                return memo[(prev, i)]
            else:
                memo[(prev, i)] = max(
                    1 + dfs(nums[i], i + 1), 
                    dfs(prev, i + 1)
                )
                return memo[(prev, i)]
        
        # case where no increasing subsequence
        return dfs(float('-inf'), 0)
        

