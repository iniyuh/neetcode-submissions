class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = len(numbers)

        def binSearch(value, l=0, r=L-1):
            if l == r: 
                if value == numbers[l]: return l
                else: return None
                
            m = (l + r) // 2

            if numbers[m] == value: return m
            elif value < numbers[m]:
                return binSearch(value, l, m-1)
            else:
                return binSearch(value, m+1, r)
        

        for i, number in enumerate(numbers):
            val = binSearch(target - number) 
            if val is not None: 
                return [i+1, val+1]
