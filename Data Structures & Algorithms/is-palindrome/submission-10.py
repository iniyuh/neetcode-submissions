class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = [char for char in s.lower() if char.isalnum()]
        l, r = 0, len(new_string) - 1

        while l < r:
            if new_string[l] != new_string[r]: return False
            else: 
                l += 1
                r -= 1
        return True