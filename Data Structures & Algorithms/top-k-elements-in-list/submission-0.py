class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)

        for num in nums: hashmap[num] += 1

        hashmap_sorted = sorted(hashmap, key=hashmap.get, reverse=True)

        res = []
        for i in range(k):
            res.append(hashmap_sorted[i])
            
        return res