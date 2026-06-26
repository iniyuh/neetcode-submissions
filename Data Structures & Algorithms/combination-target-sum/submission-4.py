class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()

        ret = []
        currArr = []

        def helper(i, currSum):
            if currSum > target or i == len(nums): return
            elif currSum == target: ret.append(currArr.copy())
            else:
                currArr.append(nums[i])
                helper(i, currSum + nums[i])
                currArr.pop()

                helper(i + 1, currSum)
        
        helper(0, 0)

        return ret