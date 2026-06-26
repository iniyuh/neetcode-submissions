class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        i = length - 1
        digits[i] += 1

        while digits[i] == 10:
            digits[i] = 0
            i -= 1
            if 0 <= i: digits[i] += 1
            else: 
                digits.insert(0, 1)
        
        return digits