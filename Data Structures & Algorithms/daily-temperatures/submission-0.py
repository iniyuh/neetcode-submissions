class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            curr = temperatures[i]
            val = 0

            for j in range(i+1, len(temperatures)):
                if curr < temperatures[j]:
                    val = j - i
                    break
                    
            result.append(val)
        
        return result