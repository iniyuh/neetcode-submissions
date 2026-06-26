class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                idx = stack.pop()[1]
                ret[idx] = i - idx
            
            stack.append((temp, i))
        
        while stack:
            ret[stack.pop()[1]] = 0
        
        return ret
