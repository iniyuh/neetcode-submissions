class Solution:
    def checkValidString(self, s: str) -> bool:
        count = 0
        p_right = 0
        p_neutral = 0

        for char in s:
            if char == '(': count += 1
            elif char == ')': count -= 1
            else: 
                if count == 0: p_neutral += 1
                else: 
                    p_right += 1
                    count -= 1

            if count < 0: 
                if 0 < p_neutral: 
                    p_neutral -= 1
                    count += 1
                elif 0 < p_right:
                    p_right -= 1
                    p_neutral += 1
                    count += 1
                else: return False

        return count == 0
        