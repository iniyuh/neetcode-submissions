class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ret = []
        currComb = []


        def dfs(i, remainder):
            if i == len(nums):
                if remainder == 0: ret.append(currComb[:])
            else:
                mult = 1

                while remainder - mult * nums[i] >= 0: 
                    currComb.append(nums[i])
                    dfs(i+1, remainder - mult * nums[i])
                    mult += 1
                
                while currComb and currComb[-1] == nums[i]: currComb.pop()

                dfs(i+1, remainder)
        
        dfs(0, target)
        return ret

