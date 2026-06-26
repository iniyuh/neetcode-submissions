class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            ret = 0

            while n != 0:
                ret += (n % 10) ** 2
                n = n // 10
            return ret
        
        slow, fast = n, helper(n)

        while slow != fast:
            slow = helper(slow)
            fast = helper(helper(fast))
        
        return slow == 1