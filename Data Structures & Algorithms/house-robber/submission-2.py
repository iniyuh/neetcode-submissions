class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        hashmap = {}
        hashmap[0] = nums[0]
        hashmap[1] = max(nums[0], nums[1])

        def evaluation(i: int) -> int:
            if i in hashmap: return hashmap[i]

            hashmap[i] = max(nums[i] + evaluation(i-2), evaluation(i-1))
            return hashmap[i]
        
        return evaluation(len(nums) - 1)

