class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}

        for num in nums: 
            val = hm.get(num, [0, num])
            val[0] -= 1
            hm[num] = val
        
        heap = list(hm.values())
        heapq.heapify(heap)

        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(heap)[1])
        return ret

