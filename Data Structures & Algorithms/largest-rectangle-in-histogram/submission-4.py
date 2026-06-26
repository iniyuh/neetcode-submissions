class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        minHeight = heights[0]
        stack = []

        for height in heights:
            minHeight = min(minHeight, height)

            if not stack: 
                stack.append((height, height))
                maxArea = max(maxArea, height)
            else:
                greaterCount = 0
                while stack and stack[-1][0] > height: 
                    h, a = stack.pop()
                    w = int(a/h)
                    greaterCount = w

                for i in range(len(stack)):
                    h, a = stack[i]
                    stack[i] = (h, a + h)
                    maxArea = max(maxArea, stack[i][1])
                
                if not stack or stack[-1][0] != height: 
                    stack.append((height, height * (1 + greaterCount)))
                    maxArea = max(maxArea, height * (1 + greaterCount))
            
            print(stack, maxArea)
        
        return max(maxArea, minHeight * len(heights))



