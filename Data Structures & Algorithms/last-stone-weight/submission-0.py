class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [stone * -1 for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            print(list(stones))
            x, y = heapq.heappop(stones), heapq.heappop(stones)
            if x < y: heapq.heappush(stones, x - y)
        
        print(list(stones))
        return -stones[0] if stones else 0

        