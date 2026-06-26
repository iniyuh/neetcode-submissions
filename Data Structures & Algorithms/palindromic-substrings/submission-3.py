class Solution:
    """
        we can use a stack to detect palindromes
        we can use two pointers to detect palindromes
        all single characters are palindromes
        we could try to create palindromes from a "seed" leftmost character using a stack
        or we could try to create palindromes for a "seed" center character using as well as 2 seed center characters using two pointers

        for every character we start with two pointers on the character and while the characters at the l and r pointer are the same we count 
            that palindrome and expand outwards by 1 on each side
        for every pair of adjacent characters we do the same but with the two pointers being on the two characters on initialization
    """
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            l, r = i, i

            while l != -1 and r != len(s) and s[l] == s[r]: 
                count += 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l != -1 and r != len(s) and s[l] == s[r]: 
                count += 1
                l -= 1
                r += 1
            
        return count
            

        

        