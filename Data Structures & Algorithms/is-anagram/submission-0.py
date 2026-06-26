class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for char in s:
            if char in hashmap: hashmap[char] += 1
            else: hashmap[char] = 1
        
        for char in t:
            if char in hashmap: hashmap[char] -= 1
            else: return False
        
        for char in hashmap:
            if hashmap[char] != 0: return False
        
        return True
        