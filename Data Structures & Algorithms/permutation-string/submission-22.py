class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        bucket = defaultdict(int)
        total = 0
        l = 0
        lastIdx = {}

        for char in s1:
            bucket[char] += 1
            total += 1
        
        b, t = bucket.copy(), total

        print(b, t)

        for r, char in enumerate(s2):
            if t == 0: return True
            elif b[char] == 0:
                if bucket[char] == 0: 
                    b, t = bucket.copy(), total
                    l = r + 1
                else:
                    while l <= lastIdx[char]:
                        b[s2[l]] += 1
                        t += 1
                        l += 1
                    b[char] -= 1
                    t -= 1
                    lastIdx[char] = r
            else:
                b[char] -= 1
                t -= 1
                lastIdx[char] = r
            
            print(b, t, char)

        return t == 0
        

