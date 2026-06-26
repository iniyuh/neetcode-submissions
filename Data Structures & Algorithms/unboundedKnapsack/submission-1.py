class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        grid = [[0] * (capacity + 1) for _ in range(len(profit))]

        # for row in grid:
        #     print(row)

        for capacity in range(1, capacity + 1):
            if capacity >= weight[0]:
                grid[0][capacity] = (capacity // weight[0]) * profit[0]

        for item in range(1, len(profit)):
            for capacity in range(1, capacity + 1):
                
                maxProfit = grid[item - 1][capacity]
                
                n = 1
                while capacity - weight[item] * n >= 0: 
                    maxProfit = max(maxProfit, profit[item] * n + grid[item - 1][capacity - weight[item] * n])
                    n += 1
                
                grid[item][capacity] = maxProfit

        return grid[-1][-1]