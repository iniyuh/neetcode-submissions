class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n

        x = 1
        y = 2
        z = x + y

        index = n - 3
        
        while index != 0:
            index -= 1
            x = y
            y = z
            z = x + y
        
        return z
        
"""
Base cases:
    Stair n-1: 1 way
    Stair n-2: 2 ways

Other cases:
    Stair x: Stair x+1 + Stair x+2


Implementing memoization is an easy win
    without: time is O(nlogn) space is O(logn)
    with: space is O(n) time is same

However, instead we can do bottom up DP:
Start with n-1 and n-2, keep iterating till 0
"""