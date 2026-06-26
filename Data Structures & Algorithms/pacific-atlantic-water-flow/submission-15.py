class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        len_r, len_c = len(heights), len(heights[0])

        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        memo = [[[0, 0] for _ in range(len_c)] for _ in range(len_r)]

        visited = set()

        def propagate(r, c, index):
            visited.add((r, c))
            memo[r][c][index] = 1
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in visited and 0 <= nr < len_r and 0 <= nc < len_c and heights[r][c] <= heights[nr][nc]:
                    propagate(nr, nc, index)

        # pacific
        for r in range(len_r):
            propagate(r, 0, 0)
        for c in range(len_c):
            propagate(0, c, 0)
        
        visited.clear()

        # atlantic
        for r in range(len_r):
            propagate(r, len_c - 1, 1)
        for c in range(len_c):
            propagate(len_r - 1, c, 1)
        
        answer = []
        for r in range(len_r):
            for c in range(len_c):
                if memo[r][c] == [1, 1]: answer.append([r, c])
        
        return answer
