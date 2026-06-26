class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accountIndex = {}

        par = {}
        rank = {}

        for i in range(len(accounts)):
            par[i] = i
            rank[i] = 0

        def find(x):
            if par[x] != x: par[x] = find(par[x])
            return par[x]

        def union(x, y):
            pX, pY = find(x), find(y)

            if rank[pX] == rank[pY]:
                rank[pX] += 1
                par[pY] = pX
            elif rank[pX] < rank[pY]: par[pX] = pY
            else: par[pY] = pX

        for i in range(len(accounts)):
            name = accounts[i][0]

            for j in range(len(accounts[i]) - 1, 0, -1):
                email = accounts[i][j]

                if email not in accountIndex: accountIndex[email] = i
                else: 
                    union(i, accountIndex[email])
                    accounts[i].pop(j)
        
        resArrs = {}

        for accIdx in range(len(accounts)):
            parIdx = find(accIdx)

            if parIdx not in resArrs: resArrs[parIdx] = accounts[accIdx]
            else: resArrs[parIdx] += accounts[accIdx][1:]

        res = []

        for val in resArrs.values():
            val[1:] = sorted(val[1:])
            res.append(val)
        
        return res




            