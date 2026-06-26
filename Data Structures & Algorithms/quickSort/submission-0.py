# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs: List[Pair], start: int, end: int) -> None:
        if start >= end: return
        
        pivot = pairs[end]

        i = start
        for j in range(start, end):
            if pairs[j].key < pivot.key:
                temp = pairs[i]
                pairs[i] = pairs[j]
                pairs[j] = temp
                i += 1
        pairs[end] = pairs[i]
        pairs[i] = pivot

        self.quickSortHelper(pairs, start, i - 1)
        self.quickSortHelper(pairs, i + 1, end)
        return
