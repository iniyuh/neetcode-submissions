class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while 1 < len(stones):
            a, b = stones.pop(), stones.pop()
            res = a - b
            if res != 0: 
                i = 0
                while i < len(stones) and stones[i] < res: i += 1
                stones.insert(i, res)
        
        return stones[0] if stones else 0