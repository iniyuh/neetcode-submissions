class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def index(target):
            l, r = 0, len(numbers)

            while l != r:
                m = (l + r) // 2

                if numbers[m] == target: return m
                elif numbers[m] < target: l = m + 1
                else: r = m

            return None
        
        for i, number in enumerate(numbers):
            remainder = target - number
            if remainder == number:
                if i + 1 < len(numbers) and numbers[i + 1] == number: return [i+1, i+2] 
            else:
                j = index(remainder)
                if j is not None: return [i+1, j+1]
        

        