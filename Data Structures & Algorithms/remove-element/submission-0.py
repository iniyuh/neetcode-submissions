class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pointer = 0

        for i in range(len(nums)):
            num = nums[i]

            if num != val:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
        
        return pointer
            
        
