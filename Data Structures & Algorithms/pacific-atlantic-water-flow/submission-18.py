class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # find all cells that can be reached from the 2 coastlines by going uphill
        # return all cells that are in both sets

        R, C = len(heights), len(heights[0])
        directions = ((0, 1), (1, 0), (-1, 0), (0, -1))

        visited = set()
        pacific = set()
        atlantic = set()

        def dfs(r, c, prev, ocean):
            if (
                r == -1 or
                c == -1 or
                r == R or
                c == C or
                (r, c) in visited or
                heights[r][c] < prev
            ): return

            ocean.add((r, c))
            visited.add((r, c))

            for dr, dc in directions:
                dfs(r+dr, c+dc, heights[r][c], ocean)
        
        # pacific
        for c in range(C): dfs(0, c, -1, pacific)
        for r in range(R): dfs(r, 0, -1, pacific)

        visited.clear()

        # atlantic
        for c in range(C): dfs(R - 1, c, -1, atlantic)
        for r in range(R): dfs(r, C - 1, -1, atlantic)

        ret = []

        for r, c in pacific:
            if (r, c) in atlantic: ret.append([r, c])
        
        return ret


