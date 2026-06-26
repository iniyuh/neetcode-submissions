class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def dfs(string, pre, re):
            if re == 0 and pre == 0: return [string]
            elif re == 0: return [string + ')' * pre]
            elif pre == 0: return dfs(string + '(', pre + 1, re - 1)
            else: return dfs(string + '(', pre + 1, re - 1) + dfs(string + ')', pre - 1, re)

        return dfs('', 0, n)