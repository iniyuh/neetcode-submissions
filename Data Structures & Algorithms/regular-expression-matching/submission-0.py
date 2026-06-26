class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        def helper(i, j, provisional=None):
            print(i, j, provisional)
            if i > len(s) or j > len(p): return False
            elif i == len(s):
                if provisional: return False
                elif j == len(p): return True
                else:
                    while j+1 < len(p) and p[j+1] == '*':
                        j += 2

                        if j == len(p): return True
                    
                    return False
            elif j == len(p): return False
            else:
                if provisional:
                    if provisional != '.' and provisional != s[i]: return False
                    else: return helper(i+1, j)
                elif j + 1 < len(p) and p[j+1] == '*':
                    return helper(i, j + 2) or helper(i, j, p[j])
                else:
                    if p[j] == '.' or s[i] == p[j]:
                        return helper(i+1, j+1)
                    else: return False
        
        return helper(0, 0)