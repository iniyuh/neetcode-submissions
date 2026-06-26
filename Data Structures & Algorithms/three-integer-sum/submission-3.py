class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ret = []

        for idx, num in enumerate(nums):
            if 0 < num: break

            if idx > 0 and num == nums[idx - 1]: continue

            l, r = idx + 1, len(nums) - 1

            while l < r:
                currSum = num + nums[l] + nums[r]
                
                if currSum < 0:
                    l += 1
                elif 0 < currSum:
                    r -= 1
                else:
                    ret.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
        
        return ret