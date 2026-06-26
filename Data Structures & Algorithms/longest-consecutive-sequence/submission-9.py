class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        
        par = {}
        rank = {}

        for num in nums:
            par[num] = num
            rank[num] = 1

        def find(i):
            if par[i] == i: return i
            else:
                par[i] = find(par[i])
                return par[i]
        
        def union(i, j):
            a, b = find(i), find(j)

            if a == b: return

            rank[a] += rank[b]
            par[b] = a
        
        for num in nums:
            if num - 1 in par:
                union(num - 1, num)
        
        return max(rank.values())

