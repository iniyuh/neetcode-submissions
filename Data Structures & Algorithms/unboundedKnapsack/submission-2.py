class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        prev = [capacity // weight[0] * profit[0] for capacity in range(0, capacity + 1)]
        print(prev)

        for item in range(1, len(profit)):
            curr = prev.copy()

            for cap in range(0, capacity + 1):
                n = 1
                while cap - weight[item] * n >= 0:
                    curr[cap] = max(curr[cap], profit[item] * n + prev[cap - weight[item] * n])
                    n += 1

            prev = curr
            print(prev)
        
        return prev[-1]