class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        curr = []

        def helper(i):
            if i == len(nums): ret.append(curr.copy())
            else:
                curr.append(nums[i])
                helper(i + 1)
                curr.pop()

                while i + 1 < len(nums) and nums[i] == nums[i + 1]: i += 1
                helper(i + 1)
        
        helper(0)
        return ret