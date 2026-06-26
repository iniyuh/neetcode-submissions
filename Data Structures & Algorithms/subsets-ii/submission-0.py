class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        curr = []
        ret = []

        def helper(i, nums, curr, ret):
            if i == len(nums): ret.append(curr.copy())
            else:
                curr.append(nums[i])
                helper(i + 1, nums, curr, ret)
                curr.pop()

                while i + 1 < len(nums) and nums[i] == nums[i + 1]: i += 1
                helper(i + 1, nums, curr, ret)
        helper(0, nums, curr, ret)
        return ret