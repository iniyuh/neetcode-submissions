class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        current_set = []
        leng = len(nums)

        def dfs(i, current_sum):
            if leng <= i: return
            elif current_sum == target:
                ret.append(current_set[:])
            else:
                if current_sum + nums[i] <= target:
                    current_set.append(nums[i])
                    dfs(i, current_sum + nums[i])
                    current_set.pop()
                    dfs(i + 1, current_sum)
                else:
                    dfs(i + 1, current_sum)
        
        dfs(0, 0)
        return ret