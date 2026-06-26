class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        currentString = ""

        def dfs(remaining, openLefts):
            nonlocal currentString

            if remaining == 0: ret.append(currentString + (")" * openLefts))
            else:
                currentString += '('
                dfs(remaining - 1, openLefts + 1)
                currentString = currentString[:-1]

                if openLefts > 0:
                    currentString += ')'
                    dfs(remaining, openLefts - 1)
                    currentString = currentString[:-1]
        
        dfs(n, 0)
        return ret
        
