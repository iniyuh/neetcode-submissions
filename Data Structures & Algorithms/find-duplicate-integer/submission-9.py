"""
Use a set: O(n) time O(n) space
Can we reduce space?

"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        visited = set()

        for num in nums: 
            if num in visited: return num
            visited.add(num)