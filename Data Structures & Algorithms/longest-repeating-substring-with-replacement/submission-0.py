class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        maxLength = 0
        hashmap = {}

        while r < len(s):
            if s[r] in hashmap:
                hashmap[s[r]] += 1

                vals = hashmap.values()
                if sum(vals) - max(vals) > k:
                    hashmap[s[l]] -= 1
                    if hashmap[s[l]] == 0: del hashmap[s[l]]
                    l += 1
                else:
                    maxLength += 1
            else:
                hashmap[s[r]] = 1

                vals = hashmap.values()
                if sum(vals) - max(vals) > k:
                    hashmap[s[l]] -= 1
                    if hashmap[s[l]] == 0: del hashmap[s[l]]
                    l += 1
                else:
                    maxLength += 1

            r += 1
        
        return maxLength
            
# l 0
# r 5
# max 5
# hash[A] = 4
# hash[B] = 1