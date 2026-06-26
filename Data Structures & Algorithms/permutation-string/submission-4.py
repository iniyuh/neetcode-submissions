class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        L1, L2 = len(s1), len(s2)
        
        def index(char):
            return ord(char) - ord('a')

        bucket = [0] * 26
        allowed = set()
        for char in s1:
            allowed.add(char)
            bucket[index(char)] += 1
        
        l, r = 0, 0
        diff = L1
        
        while diff != 0 and r < L2:
            i = index(s2[r])

            if bucket[i] > 0: 
                diff -= 1
                bucket[i] -= 1

                r += 1
            elif s2[r] in allowed:
                while s2[l] != s2[r]:
                    bucket[index(s2[l])] += 1
                    diff += 1
                    l += 1
                bucket[index(s2[l])] += 1
                diff += 1
                l += 1
            else:
                while l < r:
                    bucket[index(s2[l])] += 1
                    diff += 1
                    l += 1
                l += 1
                r = l


        return diff == 0



