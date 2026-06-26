class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """
        abc
        ab.

        abc
        abc*
        
        abc 
        abcd*

        abcdd
        abcdd*
        """

        """
        Brute force:
            DFS with bool return, should take pointer for both strings and flag for star case
            Match normally for all letters and .
            Branch on *
                This might be easier if we do the matching BACKWARDS so we see the star immediately
                Branches:
                    Skip the star character and proceed
                    Take the star character (flag set to true to indicate we are using star char)
                        Recurves both
                Branch order TBD (might be good to do star branch first if we have lots of repeating chars)
            
            POTENTIALLY COULD MEMOIZE BUT FLAG MAKES IT 3D, MAYBE ONLY MEMOIZE 2D ON POINTERS + FLAG OFF
        """
        memo = {}

        def dfs(s_idx, p_idx, flag=False):
            if s_idx == -1 and p_idx == -1 : 
                return True
            elif s_idx == -1 and p_idx != -1: 
                while p_idx != -1 and p[p_idx] == '*': p_idx -= 2
                return p_idx == -1
            elif p_idx == -1: 
                return False
            
            elif (s_idx, p_idx, flag) in memo: 
                return memo[(s_idx, p_idx, flag)]


            S, P = s[s_idx], p[p_idx]

            if P != "*" and not flag:
                if P == '.' or S == P: memo[(s_idx, p_idx, flag)] = dfs(s_idx - 1, p_idx - 1)
                else: memo[(s_idx, p_idx, flag)] = False
            elif P == '*':
                memo[(s_idx, p_idx, flag)] = dfs(s_idx, p_idx - 1, True) or dfs(s_idx, p_idx - 2)
            elif flag:
                if P == '.' or S == P: memo[(s_idx, p_idx, flag)] = dfs(s_idx - 1, p_idx, True) or dfs(s_idx - 1, p_idx - 1, False)
                else: memo[(s_idx, p_idx, flag)] = False
            
            return memo[(s_idx, p_idx, flag)]

        return dfs(len(s) - 1, len(p) - 1)






