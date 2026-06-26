class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1: return len(nums)
        par = {}
        rank = {}

        res = 1

        def find(i):
            if par[i] != i: par[i] = find(par[i])
            return par[i]
        
        def union(x, y):
            pX, pY = find(x), find(y)

            rank[pY] += rank[pX]

            nonlocal res
            res = max(res, rank[pY])

            par[pX] = pY

        for num in nums:
            if num not in par: 
                par[num] = num
                rank[num] = 1
            
                if num - 1 in par: 
                    union(num-1, num)
                if num + 1 in par: 
                    union(num, num+1)
            
        return res
            

