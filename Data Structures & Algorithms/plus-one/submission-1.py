class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1

        while -1 < i:
            digits[i] += carry
            if digits[i] >= 10: 
                carry = digits[i] // 10
                digits[i] = digits[i] % 10
                i -= 1
            else:
                carry = 0 
                break
        
        if i == -1 and carry != 0: return [carry] + digits
        
        return digits