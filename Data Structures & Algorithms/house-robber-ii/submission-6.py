class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        elif len(nums) == 1: return nums[0]

        hm = {}
        
        def helper(i, flag=None):
            if (i, flag) in hm: return hm[(i, flag)]
            elif i == 0: 
                hm[(i, flag)] = max(nums[i] + helper(i + 2, True), helper(i + 1, False))
                return hm[(i, flag)]
            elif i == len(nums) - 1: return nums[i] if not flag else 0
            elif i == len(nums): return 0
            else:
                print("For", i, "with flag", flag, "comparing", nums[i] + helper(i + 2, flag), "and", helper(i + 1, flag))
                hm[(i, flag)] = max(nums[i] + helper(i + 2, flag), helper(i + 1, flag))
                return hm[(i, flag)]
        
        return helper(0)