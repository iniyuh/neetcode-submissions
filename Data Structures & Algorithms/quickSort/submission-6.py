# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:

        def helper(l, r):
            if r - l <= 1: return

            pivotValue = pairs[r - 1].key

            pointer = l
            insert = l
            while pointer < r - 1:
                if pairs[pointer].key < pivotValue:
                    pairs[insert], pairs[pointer] = pairs[pointer], pairs[insert]
                    insert += 1
                
                pointer += 1
            
            pairs[r - 1], pairs[insert] = pairs[insert], pairs[r - 1]

            helper(l, insert)
            helper(insert + 1, r)
        
        helper(0, len(pairs))
        return pairs
        