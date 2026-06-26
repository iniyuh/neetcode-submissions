class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        leng = len(nums)

        def dfs(i, current_set, current_sum):
            if leng <= i: return
            elif current_sum == target:
                ret.append(current_set[:])
            else:
                if current_sum + nums[i] <= target:
                    dfs(i, current_set + [nums[i]], current_sum + nums[i])
                    dfs(i + 1, current_set, current_sum)
                else:
                    dfs(i + 1, current_set, current_sum)
        
        dfs(0, [], 0)
        return ret