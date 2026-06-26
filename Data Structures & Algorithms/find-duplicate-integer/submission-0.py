class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hs = set()

        for num in nums:
            if num in hs: return num
            else: hs.add(num)