class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack:
                if stack[-1][0] < temp: 
                    t = stack[-1][1]
                    res[t] = i - t
                    stack.pop()
                else: break
            stack.append((temp, i))

        return res