class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            if stack: 
                while stack and stack[-1][1] < temperatures[i]:
                    j = stack.pop()[0]
                    result[j] = i - j
            stack.append((i, temp))
        
        return result

                