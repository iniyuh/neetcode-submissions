class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s, f = 0, 0

        while True:
            s = nums[s]
            f = nums[nums[f]]

            if s == f:
                s2 = 0
                while s != s2:
                    s = nums[s]
                    s2 = nums[s2]
                
                return s2