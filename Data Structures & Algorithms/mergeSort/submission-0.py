# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        solution.mmergeSort(pairs, 0, len(pairs))

        return pairs

    def mmergeSort(self, pairs, s, e):
        if e - s <= 1: return

        m = (e - s) // 2 + s
        solution.mmergeSort(pairs, s, m)
        solution.mmergeSort(pairs, m, e)

        solution.merge(pairs, pairs[s:m], pairs[m:e], s, m, e)

        return
    
    def merge(self, pairs, leftArray, rightArray, s, m, e):
        k = s
        i = 0
        j = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i].key <= rightArray[j].key:
                pairs[k] = leftArray[i]
                i += 1
            else:
                pairs[k] = rightArray[j]
                j += 1
            k += 1
        
        while i < len(leftArray):
            pairs[k] = leftArray[i]
            i += 1
            k += 1
        while j < len(rightArray):
            pairs[k] = rightArray[j]
            j += 1
            k += 1

        return
