class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        length = len(nums)

        def helper(i, tailBanned):
            if length <= i: return 0
            if (i, tailBanned) in memo: return memo[(i, tailBanned)]

            take = nums[i] + helper(i + 2, tailBanned) - (nums[i] * tailBanned * (i == length - 1))

            leave = helper(i + 1, tailBanned)

            print("At", nums[i], "take is", take, "and leave is", leave)
            res = max(take, leave)
            memo[(i, tailBanned)] = res
            return res
        
        return max(helper(1, 0), nums[0] + helper(2, 1))
