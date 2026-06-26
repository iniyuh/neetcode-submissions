class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = {}

        for num in nums:
            if num not in hashmap: hashmap[num] = True
            else: return True
        return False