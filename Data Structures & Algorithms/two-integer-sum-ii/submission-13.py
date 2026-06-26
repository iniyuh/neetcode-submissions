class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prev = None

        def binarySearch(value, l):
            r = len(numbers)

            while l < r:
                m = (l + r) // 2

                if numbers[m] < value: l = m + 1
                elif value < numbers[m]: r = m
                else: return m
            
            return None
            


        for i, num in enumerate(numbers):
            if prev and prev == num: continue


            remainder = target - num
            if remainder >= num:
                index = binarySearch(remainder, i + 1)
                if index: return [i + 1, index + 1]


            prev = num