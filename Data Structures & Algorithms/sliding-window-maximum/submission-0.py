class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        def findMax(l, r):
            mVal = nums[l]
            mIndex = l
            for i in range(l+1, r+1):
                if mVal < nums[i]:
                    mVal = nums[i]
                    mIndex = i
            print(l, "to", r, "max:", mVal, ", index:", mIndex)
            return (mIndex, mVal)
        
        
        l, r = 0, k - 1

        mIndex, mVal = findMax(l, r)
        res = [mVal]

        while r + 1 < len(nums):
            l, r = l + 1, r + 1

            if nums[r] > mVal:
                mIndex, mVal = r, nums[r]
            elif l - 1 == mIndex:
                mIndex, mVal = findMax(l, r)
            
            res.append(mVal)
        
        return res