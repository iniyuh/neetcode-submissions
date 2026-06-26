class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = defaultdict(int)
        total = len(t)

        for char in t: counts[char] += 1

        remainder = total
        l = 0

        ret = ""

        for r in range(len(s)):
            char = s[r]

            # skippable
            if char not in counts and remainder == total: l += 1
            
            # hit
            else:                                   # hit
                counts[char] -= 1

                # decrement if needed
                if counts[char] >= 0: remainder -= 1
                
                # candidate found
                if remainder == 0:
                    
                    # prune left if we had surplus 
                    while l < r and (s[l] not in counts or counts[s[l]] < 0):
                        if s[l] in counts:
                            counts[s[l]] += 1
                        l += 1

                    # evaluate candidate
                    if (r - l + 1) < len(ret) or not ret:
                        ret = s[l:r+1]
                    
                    # remove leftmost productive letter
                    counts[s[l]] += 1
                    remainder += 1
                    l += 1

                    # prune left
                    while l < r and s[l] not in counts: l += 1
        
        return ret



                




        