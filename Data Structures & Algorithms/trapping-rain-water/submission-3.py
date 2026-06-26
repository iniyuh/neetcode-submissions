class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        res = 0

        while l < r:
            if lMax <= rMax:
                l += 1
                res += max(lMax - height[l], 0)
                lMax = max(lMax, height[l])
            else:
                r -= 1
                res += max(rMax - height[r], 0)
                rMax = max(rMax, height[r])

        

        return res
