class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [0] * (n + 1)
        
        def count(num):
            if num in memo: return memo[num]

            memo[num] = (0b1 & num) * 1 + count(num >> 1)
            
            return memo[num]
        
        ret = [0] * (n + 1)
        for i in range(n+1): ret[i] = (count(i))
        return ret
        
