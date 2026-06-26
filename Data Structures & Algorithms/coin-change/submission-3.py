class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def minCoins(remainder):
            if remainder == 0: return 0
            elif remainder in memo: return memo[remainder]
            else:
                ret = float('inf')

                for coin in coins:
                    if remainder - coin >= 0: ret = min(ret, 1 + minCoins(remainder - coin))
                
                memo[remainder] = ret
                return ret
        
        ret = minCoins(amount)
        return ret if ret != float('inf') else -1

        
