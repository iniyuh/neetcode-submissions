class Solution:
    

    def findKthLargest(self, nums: List[int], k: int) -> int:
        def quickSelect(l, r):
            pivot = nums[r]
            p = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[p], nums[r] = nums[r], nums[p]

            if p < len(nums) - k: return quickSelect(p+1, r)
            elif len(nums) - k < p: return quickSelect(l, p-1)
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)
