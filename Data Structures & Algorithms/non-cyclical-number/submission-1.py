class Solution:
    def isHappy(self, n: int) -> bool:
        memo = set()

        while n != 1:
            if n in memo: return False
            else:
                memo.add(n)
                temp = 0
                while n != 0:
                    temp += (n % 10) ** 2
                    n = n // 10
                n = temp

        return True