class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        par = [i for i in range(len(accounts))]

        hm = {}

        def find(i):
            if par[i] == i: return i
            else:
                par[i] = find(par[i])
                return par[i]
        
        def union(i, j):
            a, b = find(i), find(j)
            
            if a == b: return

            if a < b: par[b] = a
            else: par[a] = b

        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                email = account[j]

                if email not in hm:
                    hm[email] = i
                else:
                    union(hm[email], i)
        
        ret = []
        hm2 = {}
        for i in range(len(accounts)):
            print(i, find(i))
        for i, account in enumerate(accounts):
            if find(i) == i: 
                hm2[i] = len(ret)
                ret.append([account[0], set(account[1:])])
            else:
                print(i, find(i))
                idx = hm2[find(i)]
                ret[idx][1].update(account[1:])

        final = []
        for item in ret: final.append([item[0]] + sorted(list(item[1])))

        return final

        
