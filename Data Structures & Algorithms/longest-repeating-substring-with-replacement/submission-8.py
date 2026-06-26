class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        maxf = 0
        l = 0
        maxLength = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            maxf = max(maxf, counts[s[r]])

            while r - l + 1 - maxf > k:
                counts[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)

        return maxLength