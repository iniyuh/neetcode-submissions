class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        current_set = []

        def dfs(i):
            if i >= len(nums):
                ret.append(current_set[:])
            else:
                dfs(i+1)
                current_set.append(nums[i])
                dfs(i+1)
                current_set.pop()
            
        dfs(0)
        return ret
            