class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)

        i = 0
        prev = 0
        req = set()
        ret = []
        while i < len(s):
            
            counts[s[i]] -= 1
            if counts[s[i]] > 0: req.add(s[i])

            i += 1
            while req:
                counts[s[i]] -= 1

                if counts[s[i]] == 0: req.discard(s[i])
                else: req.add(s[i])

                i += 1
            
            ret.append(i - prev)
            prev = i
        
        return ret
        
