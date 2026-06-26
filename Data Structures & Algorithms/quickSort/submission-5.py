# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        
        def helper(l, r):
            if r <= l: return

            pivot = pairs[r]

            swapIdx = l

            for i in range(l, r+1):
                if pairs[i].key < pivot.key:
                    pairs[swapIdx], pairs[i] = pairs[i], pairs[swapIdx]
                    swapIdx += 1
            
            pairs[r], pairs[swapIdx] = pairs[swapIdx], pairs[r]

            helper(l, swapIdx - 1)
            helper(swapIdx + 1, r)
        
        helper(0, len(pairs) - 1)
        return pairs
            
