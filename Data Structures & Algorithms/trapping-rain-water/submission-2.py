class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        l_max, r_max = 0, 0
        flag = True

        res = 0

        while l < r:
            bound = min(l_max, r_max)
            h = height[l] if flag else height[r]
            if h < bound:
                res += bound - h
                print("L:" if flag else "R:", l if flag else r, "val:", bound - h)


            l_max = max(l_max, height[l])
            r_max = max(r_max, height[r])

            if height[l] <= height[r]: 
                l += 1
                flag = True
            else: 
                r -= 1
                flag = False
        
        return res
