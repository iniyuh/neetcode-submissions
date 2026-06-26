class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []

        def helper(i, currSum, currComb):
            if currSum == target: ret.append(currComb.copy())
            elif i == len(nums): return
            else:
                j = 0

                while currSum + j * nums[i] <= target:
                    helper(i + 1, currSum + j * nums[i], currComb)
                    currComb.append(nums[i])

                    j += 1

                for _ in range(j): currComb.pop()

        helper(0, 0, [])
        return ret
                
                