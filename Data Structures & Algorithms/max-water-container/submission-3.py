"""
lets use a two pointer approach starting on both ends
area = min(h_i, h_j) * (j - i + 1)
we move one pointer at a time, always move the one at the smaller height
tiebreak arbitrarily
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            h = min(heights[l], heights[r])
            maxArea = max(maxArea, h * (r - l))

            if heights[l] <= heights[r]: l += 1
            else: r -= 1
        
        return maxArea