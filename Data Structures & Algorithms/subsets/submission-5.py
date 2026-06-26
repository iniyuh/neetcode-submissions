class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        currSet = []

        def dfs(i):
            if i == len(nums): ret.append(currSet[:])
            else:
                dfs(i+1)

                currSet.append(nums[i])
                dfs(i+1)
                currSet.pop()
        
        dfs(0)
        return ret