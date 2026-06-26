class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        directions = ((1, 0), (0, 1), (1, 1), (1, -1))
        ret = []

        curr = [['.' for _ in range(n)] for _ in range(n)]
        # print("Initial curr", curr)
        blacklist = defaultdict(int)

        def updateBlacklist(r, c, expand):
            if expand: blacklist[(r, c)] += 1
            else: 
                if blacklist[(r, c)] == 1: del blacklist[(r, c)]
                else: blacklist[(r, c)] -= 1

            for dr, dc in directions:
                nr, nc = r+dr, c+dc

                while nr != -1 and nc != -1 and nr != n and nc != n:
                    if expand: blacklist[(nr, nc)] += 1
                    else: 
                        if blacklist[(nr, nc)] == 1: del blacklist[(nr, nc)]
                        else: blacklist[(nr, nc)] -= 1
                    nr, nc = nr+dr, nc+dc

        def helper(i, r, c):
            if i == n: 
                # print(curr)
                ret.append(["".join(arr) for arr in curr])
            elif r == n or c == n: return
            else:
                if (r, c) not in blacklist:

                    curr[r][c] = 'Q'
                    # print("Testing queen at", r, c)
                    updateBlacklist(r, c, True)
                    # print(curr)
                    # print(blacklist)
                    if c == n - 1: helper(i + 1, r + 1, 0)
                    else: helper(i + 1, r, c + 1)

                    curr[r][c] = '.'
                    updateBlacklist(r, c, False)
                    if c == n - 1: helper(i, r + 1, 0)
                    else: helper(i, r, c + 1)
                else:
                    if c == n - 1: helper(i, r + 1, 0)
                    else: helper(i, r, c + 1)

        helper(0, 0, 0)
        return ret
        