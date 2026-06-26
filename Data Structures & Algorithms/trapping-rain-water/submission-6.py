class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        maxL = height[l]
        maxR = height[r]
        globalMin = min(maxL, maxR)

        volume = 0

        while l < r:
            if height[l] < height[r]:
                l += 1
                volume += max(0, globalMin - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                volume += max(0, globalMin - height[r])
                maxR = max(maxR, height[r])
            globalMin = min(maxL, maxR)
        
        return volume