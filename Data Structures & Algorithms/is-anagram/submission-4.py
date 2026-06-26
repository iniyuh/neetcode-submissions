class Solution:
    @staticmethod
    def index(char):
        return ord(char) - ord('a')

    def isAnagram(self, s: str, t: str) -> bool:
        counterS = [0] * 26
        counterT = [0] * 26

        for char in s:
            counterS[self.index(char)] += 1
        
        for char in t:
            counterT[self.index(char)] += 1
        
        counterS = tuple(counterS)
        counterT = tuple(counterT)

        return counterS == counterT