class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []

        def helper(i, nums, curr, ret):
            if i == len(nums): ret.append(curr.copy())
            else:
                curr.append(nums[i])
                helper(i + 1, nums, curr, ret)
                curr.pop()

                helper(i + 1, nums, curr, ret)

        helper(0, nums, curr, ret)
        return ret