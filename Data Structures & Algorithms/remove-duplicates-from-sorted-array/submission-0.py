class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertionPointer = 0
        i = 0
        prev = None

        for j, curr in enumerate(nums):
            if curr != prev:
                nums[j], nums[i] = nums[i], nums[j]

                i += 1
                prev = curr
        
        return i




