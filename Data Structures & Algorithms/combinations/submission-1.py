class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret = []

        def helper(i, curr):
            if len(curr) == k: ret.append(curr.copy())
            elif i > n: return
            else:
                for j in range(i, n + 1):
                    curr.append(j)
                    helper(j + 1, curr)
                    curr.pop()
        
        helper(1, [])
        return ret