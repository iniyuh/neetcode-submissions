class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def calcArea(i, j):
            return min(heights[i], heights[j]) * (j - l)

        l, r = 0, len(heights) - 1
        maxArea = 0

        while l < r:
            maxArea = max(maxArea, calcArea(l, r))
            if heights[l] < heights[r]: l += 1
            else: r -= 1

        return maxArea