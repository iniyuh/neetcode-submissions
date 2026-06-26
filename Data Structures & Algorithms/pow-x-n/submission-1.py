class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x

        pos = n > 0
        if not pos: n *= -1

        comps = [(x, 1)]

        while 2 * comps[-1][1] <= n:
            comps.append((comps[-1][0] * comps[-1][0], comps[-1][1] * 2))
        
        ret = 1
        rem = n

        while rem != 0:
            val, i = comps.pop()

            if i <= rem: 
                ret *= val
                rem -= i

        return ret if pos else 1/ret
        

