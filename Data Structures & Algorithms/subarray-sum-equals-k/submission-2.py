class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total = 0
        hashmap = {0 : 1}
        res = 0

        for num in nums:
            total += num

            res += hashmap.get(total - k, 0)
            hashmap[total] = 1 + hashmap.get(total, 0)
        
        return res

            

