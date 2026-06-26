class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        maxLength = 0

        def dfs(i, prev=None):
            if i in memo: return memo[i]
            elif i == len(nums): return 0
            else:
                duplicate = nums[i]
                max_ = 0

                for j in range(i + 1, len(nums)):
                    if duplicate == nums[j]: continue
                    else: duplicate = nums[j]

                    val = dfs(j)
                    if nums[i] < nums[j]: max_ = max(max_, val)
                
                memo[i] = max_ + 1
                nonlocal maxLength
                maxLength = max(maxLength, memo[i])
                print(nums[i], memo[i])
                return memo[i]
        
        dfs(0)
        return maxLength
