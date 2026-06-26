class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        hm = {}

        def helper(l, r):
            if r < l: return 0
            if l == r: return nums[l-1]*nums[l]*nums[l+1]
            if (l, r) in hm: return hm[(l, r)]

            hm[(l, r)] = 0
            for i in range(l, r+1): hm[(l, r)] = max(hm[(l, r)], nums[l-1]*nums[i]*nums[r+1] + helper(l, i-1) + helper(i+1, r))

            return hm[(l, r)]
        
        return helper(1, len(nums) - 2)
