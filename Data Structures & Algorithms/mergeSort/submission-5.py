# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair], l: int = None, r: int = None) -> List[Pair]:
        if not pairs: return []
        
        def ms(l, r):
            if r - l == 1: return

            m = (l + r) // 2

            ms(l, m)
            ms(m, r)

            merge(l, pairs[l:m], pairs[m:r])
        

        def merge(p, arr1, arr2):
            l1, l2 = 0, 0

            while l1 < len(arr1) and l2 < len(arr2):
                if arr1[l1].key <= arr2[l2].key:
                    pairs[p] = arr1[l1]
                    l1 += 1
                else:
                    pairs[p] = arr2[l2]
                    l2 += 1
                
                p += 1
            
            while l1 < len(arr1):
                pairs[p] = arr1[l1]
                l1 += 1
                p += 1
            
            while l2 < len(arr2):
                pairs[p] = arr2[l2]
                l2 += 1
                p += 1
    
        ms(0, len(pairs))
        return pairs

