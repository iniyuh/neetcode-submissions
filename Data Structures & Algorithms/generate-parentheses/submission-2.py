class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []

        def dfs(currString, openCount):
            if len(currString) == 2 * n: 
                if openCount == 0: ret.append(currString)
            else:
                if openCount > 0: dfs(currString + ')', openCount - 1)
                dfs(currString + '(', openCount + 1)
        
        dfs('', 0)
        return ret
