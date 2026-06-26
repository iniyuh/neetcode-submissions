class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counter = {}
        total = len(t)
        for char in t:
            counter[char] = 1 + counter.get(char, 0)
        
        l = 0
        minLength = float('inf')
        minL, minR = None, None

        for r, char in enumerate(s):
            print(s[l:r+1])
            if char in counter:
                counter[char] -= 1
                total -= 1 if counter[char] >= 0 else 0

                while total == 0:
                    if (r - l + 1) < minLength:
                        minLength = r - l + 1
                        minL, minR = l, r
                    
                    if s[l] in counter: 
                        counter[s[l]] += 1
                        total += 1 if counter[s[l]] > 0 else 0
                    
                    l += 1
        
        print(minL, minR)
        return s[minL:minR+1] if minL is not None else ''
        
