class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []

        def helper(i):
            if i == len(nums): ret.append(curr.copy())
            else:
                curr.append(nums[i])
                helper(i + 1)
                curr.pop()

                helper(i + 1)
        
        helper(0)
        return ret
