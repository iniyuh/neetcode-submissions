# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        def insert(origin, destination):
            if origin == destination: return

            temp = pairs[origin]

            for i in range(origin, destination, -1):
                pairs[i] = pairs[i-1]

            pairs[destination] = temp
        
        res = []
        sortedIndex = 0

        for origin in range(len(pairs)):
            inbound = pairs[origin]


            destination = 0
            while destination < sortedIndex and pairs[destination].key <= inbound.key: 
                destination += 1
            
            insert(origin, destination)

            res.append(pairs[:])
            sortedIndex += 1
        
        return res

        
