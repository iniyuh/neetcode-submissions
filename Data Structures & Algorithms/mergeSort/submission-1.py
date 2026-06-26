# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def merge(s, m, e):
            l_sub = pairs[s:m]
            r_sub = pairs[m:e]

            length_l = len(l_sub)
            length_r = len(r_sub)

            curr, l, r = s, 0, 0

            while l < len(l_sub) or r < len(r_sub):
                if r == length_r or (l < length_l and l_sub[l].key <= r_sub[r].key):
                    pairs[curr] = l_sub[l]
                    l += 1
                else:
                    pairs[curr] = r_sub[r]
                    r += 1
                curr += 1


        def helper(s, e):
            if e - s <= 1: return

            m = (s + e) // 2

            helper(s, m) # 0, 1
            helper(m, e) # 1, 2
            merge(s, m, e) # 0, 1, 2
        
        helper(0, len(pairs))
        return pairs