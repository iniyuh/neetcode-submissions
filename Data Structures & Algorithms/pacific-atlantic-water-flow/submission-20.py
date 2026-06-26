class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        multi source bfs?
        dfs from the pacific wall and atlantic wall then intersect reached cells?
        use a visited set per ocean to prevent redundancy

        for our first solution, let's just dfs from all cells of both seeds and
        then intersect our sets
        """
        R, C = len(heights), len(heights[0])
        directions = ((0,1),(1,0),(-1,0),(0,-1))
        
        pacificSet = set()
        atlanticSet = set()

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr == R or nc == C or nr == -1 or nc == -1 or (nr, nc) in visited: continue

                if heights[nr][nc] >= heights[r][c]: 
                    dfs(nr, nc, visited)
                
        
        # seed from pacific
        for r in range(R):
            dfs(r, 0, pacificSet)
        for c in range(C):
            dfs(0, c, pacificSet)
        
        # seed from atlantic
        for r in range(R):
            dfs(r, C - 1, atlanticSet)
        for c in range(C):
            dfs(R - 1, c, atlanticSet)
        

        intersection = []

        for r, c in pacificSet:
            if (r, c) in atlanticSet: intersection.append([r, c])
        
        return intersection

        