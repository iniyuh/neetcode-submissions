"""
Use a set: O(n) time O(n) space
Can we reduce space?
Yes by utilize the given nums array. 
    How can we do so without ruining the data?
    By altering it in some "dimension" that isn't relevant to the scope of the problem
        For example, signage. We can flip the sign of things we've seen so if we find a 
        1 we can go to the 0th index and make it negative whatever it was and if it's already
        negative, we've found our duplicate based on the index
Yes by utilizing fast and slow pointers
    If you treat the value as a pointer to an index then if we only had everything once
    we would have a linked list containing all numbers/indices
    However due to the duplicate we will have 2 nodes pointing to the same index 
    which introduces a cycle.
    Fast and slow pointer until pointers meet to find the cycle
    Then create third pointer at start and keep iterating to meet to find cycle start
    aka the duplicate
    NOTE: If we say had a 0 at index 0 we would get stuck. This approach works because we know numbers
    are 1 to n and not 0 to n-1
"""

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast: break
        
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[fast]

            if slow == fast: break
        
        return slow