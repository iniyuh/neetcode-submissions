# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs: return []
        
        ret = [pairs.copy()]

        for i in range(1, len(pairs)):
            j = i - 1
            print(j, pairs[j].key, pairs[j+1].key)
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                print("swap")
                pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                j -= 1
            
            ret.append(pairs.copy())
        
        return ret[:]