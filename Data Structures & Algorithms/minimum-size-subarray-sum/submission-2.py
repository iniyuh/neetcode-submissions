class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ret = float('inf')
        currSum = nums[0]

        l, r = 0, 0

        while l <= r:
            if currSum >= target: 
                print("hit", currSum, l, r)
                ret = min(ret, r - l + 1)
                currSum -= nums[l]
                l += 1
            else:
                r += 1
                if r == len(nums): break
                currSum += nums[r]


        return int(ret) if ret != float('inf') else 0