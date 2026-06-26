class Solution:
    def jump(self, nums: List[int]) -> int:
        curr = {0}
        next_ = set()
        count = 0

        while True:
            for idx in curr:
                if idx == len(nums) - 1: return count
                for dest in range(idx+1, idx+nums[idx]+1): next_.add(dest)
            
            count += 1
            curr = next_
            next_ = set()
