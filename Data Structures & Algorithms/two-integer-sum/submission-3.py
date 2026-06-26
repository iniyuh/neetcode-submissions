class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            hashmap[num] = i

        for i, num in enumerate(nums):
            if (target - num) in hashmap and hashmap[target - num] != i: return [i, hashmap[target - num]]