class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for h in heights + [0]:
            w = 0
            while stack and stack[-1][0] > h:
                ph, pw = stack.pop()
                w += pw
                maxArea = max(maxArea, w * ph)
            stack.append((h, w + 1))
        
        return maxArea
