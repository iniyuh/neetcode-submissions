class Solution:
    def isHappy(self, n: int) -> bool:
        def helper(n):
            s = str(n)
            ret = 0

            for char in s:
                ret += int(char) ** 2
            
            return ret
        
        visited = set()
        while n != 1:
            if n in visited: return False

            visited.add(n)
            n = helper(n)

        return True