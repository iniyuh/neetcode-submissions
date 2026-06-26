class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr, ret = [], []

        def helper(i, curr, ret):
            if len(curr) == k: ret.append(curr.copy())
            elif i > n: return
            else:
                curr.append(i)
                helper(i + 1, curr, ret)
                curr.pop()
                
                helper(i + 1, curr, ret)
        
        helper(1, curr, ret)
        return ret
