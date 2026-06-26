class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        hm = {}

        # consider sorting descending and backtracking.
        
        def minCoins(i, remainder):
            if remainder == 0: return 0
            elif i == len(coins): return float('inf')
            elif (i, remainder) in hm: return hm[(i, remainder)]
            else:
                ret = float('inf')
                count = 0

                while remainder - count * coins[i] >= 0:
                    ret = min(ret, count + minCoins(i + 1, remainder - count * coins[i]))
                    count += 1

                hm[(i, remainder)] = ret
                return ret
        
        ret = minCoins(0, amount)
        return ret if ret != float('inf') else -1
