# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.partition(pairs, 0, len(pairs))
        return pairs

    def partition(self, pairs, l, r):
        if l < r - 1:
            m = (l + r) // 2

            self.partition(pairs, l, m)
            self.partition(pairs, m, r)

            self.merge(pairs, l, pairs[l:m], pairs[m:r])
    
    def merge(self, pairs, index, left, right):
        i, j = 0, 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[index] = left[i]
                i += 1
            else:
                pairs[index] = right[j]
                j += 1
            
            index += 1
        
        while i < len(left):
            pairs[index] = left[i]
            i += 1
            index += 1
        
        while j < len(right):
            pairs[index] = right[j]
            j += 1
            index += 1

        return
        


