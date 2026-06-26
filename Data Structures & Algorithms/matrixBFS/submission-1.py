class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))

        queue = [(0, 0, set(), 0)]
        ret = float('inf')

        while queue:
            r, c, visited, distance = queue.pop()

            if not (
                distance >= ret or
                r == -1 or
                c == -1 or
                r == R or
                c == C or
                (r, c) in visited or
                grid[r][c] == 1
            ): 
                if r == R - 1 and c == C - 1: ret = min(ret, distance)
                else:
                    newVisited = {(r, c)}
                    for item in visited: newVisited.add(item)

                    for dr, dc in directions:
                        queue.append((r+dr, c+dc, newVisited, distance + 1))
            
        return ret if ret != float('inf') else -1
