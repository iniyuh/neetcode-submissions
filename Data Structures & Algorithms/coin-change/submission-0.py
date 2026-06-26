class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        remainder = amount
        coinCount = float('inf')

        prev = [float('inf')] * (amount + 1)
        curr = [-1] * (amount + 1)

        for coin in coins:
            for amount in range(len(curr)):
                # leave it
                minCount = prev[amount]

                # take it
                if amount - coin == 0: minCount = 1
                elif amount - coin > 0:
                    minCount = min(minCount, 1 + curr[amount - coin])
                
                curr[amount] = minCount
            prev = curr

        return prev[-1] if prev[-1] != float('inf') else -1
        
                
                

