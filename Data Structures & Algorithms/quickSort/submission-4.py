# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def helper(s, e):
            if e - s <= 1: return

            pivot_element = pairs[e - 1]
            left = s
            for i in range(s, e - 1):
                if pairs[i].key < pivot_element.key:
                    pairs[left], pairs[i] = pairs[i], pairs[left]
                    left += 1

            pairs[left], pairs[e - 1] = pairs[e - 1], pairs[left]

            helper(s, left)
            helper(left + 1, e)
        
        helper(0, len(pairs))
        return pairs
            
