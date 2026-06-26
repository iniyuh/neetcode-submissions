class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}

        for i, char in enumerate(s):
            hashmap[char] = i

        l, r = 0, 0
        quota = 0
        ret = []
        while r < len(s):
            quota = max(quota, hashmap[s[r]])

            if r == quota: 
                ret.append(r - l + 1)
                l = r + 1

            r += 1

        return ret
