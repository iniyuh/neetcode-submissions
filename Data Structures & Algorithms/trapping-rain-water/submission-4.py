class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1

        cap = min(height[l], height[r])

        ret = 0

        while l <= r:
            cap = max(min(height[l], height[r]), cap)

            if height[l] <= height[r]:
                ret += cap - height[l]
                l += 1
            else:
                ret += cap - height[r]
                r -= 1
        
        return ret