class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalnum()).lower()
        print(s)
        r = len(s) // 2
        l = r if len(s) % 2 == 0 else r + 1
        print(s[:r])
        print(s[l:])
        return s[:l] == s[r:][::-1]
        