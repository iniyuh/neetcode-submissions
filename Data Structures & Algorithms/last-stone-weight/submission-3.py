class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-1 * stone for stone in stones]
        heapq.heapify(maxHeap)

        while len(maxHeap) > 1:
            bigger, smaller = -1 * heapq.heappop(maxHeap), -1 * heapq.heappop(maxHeap)
            res = bigger - smaller
            if res != 0: heapq.heappush(maxHeap, -1 * res)

        
        if len(maxHeap) == 0: return 0
        else: return -1 * maxHeap[0]