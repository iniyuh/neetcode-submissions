class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def binSearch(value):
            l, r = 0, len(numbers) - 1

            while l <= r:
                m = (l + r) // 2

                if numbers[m] == value: return m
                elif value < numbers[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            return None
        

        for i, number in enumerate(numbers):
            val = binSearch(target - number) 
            if val is not None: 
                return [i+1, val+1]
