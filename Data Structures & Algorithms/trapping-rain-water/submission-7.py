class Solution:
    def trap(self, height: List[int]) -> int:
        maxFromLeft = [height[0]] * len(height)
        maxFromRight = [height[-1]] * len(height)

        for i in range(1, len(height)):
            maxFromLeft[i] = max(maxFromLeft[i-1], height[i])

        for i in range(len(height) - 2, -1, -1):
            maxFromRight[i] = max(maxFromRight[i+1], height[i])
        

        ret = 0

        for i in range(len(height)):
            ret += max(min(maxFromLeft[i], maxFromRight[i]) - height[i], 0)
        
        return ret