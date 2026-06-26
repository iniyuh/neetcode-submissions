# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs: return pairs
        
        def merge(l, r):
            if l == r: return [pairs[l]]
            else:
                m = (l + r) // 2
                left = merge(l, m)
                right = merge(m+1, r)
                i, j = 0, 0

                z = l

                while i < len(left) and j < len(right):
                    if left[i].key <= right[j].key:
                        pairs[z] = left[i]
                        i += 1
                    else:
                        pairs[z] = right[j]
                        j += 1
                    
                    z += 1
                
                while i < len(left):
                    pairs[z] = left[i]
                    i += 1
                    z += 1
                
                while j < len(right):
                    pairs[z] = right[j]
                    j += 1
                    z += 1
                
                return pairs[l:r+1]

        merge(0, len(pairs) - 1)

        return pairs