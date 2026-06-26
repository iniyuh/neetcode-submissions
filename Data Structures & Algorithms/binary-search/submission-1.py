class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binSearch(start, end, target):
            if end <= start: return -1

            m = (end - start) // 2 + start
            val = nums[m]
            if val == target: return m
            elif target < val: return binSearch(start, m, target)
            else: return binSearch(m + 1, end, target)
        
        return binSearch(0, len(nums), target)
