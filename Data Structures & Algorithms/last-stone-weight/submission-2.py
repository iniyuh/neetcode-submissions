class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            a, b = heapq.heappop(stones) * -1, heapq.heappop(stones) * -1
            z = a - b
            heapq.heappush(stones, z * -1)
        return stones[0] * -1 if len(stones) == 1 else 0