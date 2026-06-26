class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        curr = 1
        i = 1

        factorial_r = 1
        factorial_d = 1

        while i <= (m + n - 2):
            curr *= i

            if i == n - 1: factorial_r = curr
            if i == m - 1: factorial_d = curr
            
            i += 1
        
        return int(curr/(factorial_r * factorial_d))
