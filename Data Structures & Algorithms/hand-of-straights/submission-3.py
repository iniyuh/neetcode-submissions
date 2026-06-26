class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()

        counts = Counter(hand)

        ordered = []
        tempSet = set()
        for num in hand:
            if num not in tempSet: 
                ordered.append(num)
                tempSet.add(num)
        
        req = defaultdict(int)
        prev = None

        for num in ordered:
            count = counts[num]
            quota = req[num] if num in req else None

            if not quota:
                for i in range(1, groupSize):
                    req[num+i] += count
            elif num != prev + 1 or count < quota: return False
            else:
                remainder = count - quota
                del req[num]

                if remainder > 0:
                    for i in range(1, groupSize):
                        req[num+i] += remainder
            
            prev = num
        
        return not req









