class Solution:
    def jump(self, nums: List[int]) -> int:
        L = len(nums)
        memo = {}

        def dfs(i):
            if i == L - 1: return 0
            if i in memo: return memo[i]

            minVal = float("inf")

            for j in range(1, nums[i] + 1):
                if i+j >= L: break
                minVal = min(minVal, dfs(i+j))

            memo[i] = 1 + minVal
            return memo[i]
        
        ret = int(dfs(0))
        for key, val in memo.items():
            print(key, val)
        return ret