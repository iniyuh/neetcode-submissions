class Solution:
    def countBits(self, n: int) -> List[int]:
        def count(num):
            count = 0

            while num:
                if 0b1 & num: count += 1
                num = num >> 1
            
            return count
        
        ret = [0] * (n + 1)
        for i in range(n+1): ret[i] = (count(i))
        return ret
        
