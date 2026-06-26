class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        
        ret = x
        n_ = abs(n)
        for i in range(n_ - 1):
            ret *= x
        return ret if n_ == n else 1/ret