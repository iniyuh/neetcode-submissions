# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        sortedIndex = -1
        
        for _ in range(len(pairs)):
            left = sortedIndex
            while left > -1 and pairs[left].key > pairs[left + 1].key:
                pairs[left], pairs[left+1] = pairs[left+1], pairs[left]
                left -= 1

            sortedIndex += 1
            res.append(pairs[:])
        
        return res
