class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        hm = {}

        def helper(i, j, provisional=None):
            if (i, j, provisional) in hm: return hm[(i, j, provisional)]
            elif i > len(s) or j > len(p): return False
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
                    if provisional != '.' and provisional != s[i]: hm[(i, j, provisional)] = False
                    else: hm[(i, j, provisional)] = helper(i+1, j)
                elif j + 1 < len(p) and p[j+1] == '*':
                    hm[(i, j, provisional)] = helper(i, j + 2) or helper(i, j, p[j])
                else:
                    if p[j] == '.' or s[i] == p[j]:
                        hm[(i, j, provisional)] = helper(i+1, j+1)
                    else: hm[(i, j, provisional)] = False
                
                return hm[(i, j, provisional)]
        
        return helper(0, 0)