class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs(seed, visited):
            if seed in visited: return
            else:
                visited.add(seed)

                r, c = seed
                for dr, dc in directions:
                    if  r + dr < R and c + dc < C and 0 <= r + dr and 0 <= c + dc and heights[r + dr][c + dc] >= heights[r][c]:
                        dfs((r + dr, c + dc), visited)


        pacific_seeds = []
        atlantic_seeds = []
        for r in range(R):
            pacific_seeds.append((r, 0))
            atlantic_seeds.append((r, C - 1))
        for c in range(C):
            pacific_seeds.append((0, c))
            atlantic_seeds.append((R - 1, c))

        pacific_visited = set()
        for seed in pacific_seeds:
            dfs(seed, pacific_visited)
        
        atlantic_visited = set()
        for seed in atlantic_seeds:
            dfs(seed, atlantic_visited)

        return [[item[0], item[1]] for item in list(pacific_visited.intersection(atlantic_visited))]



        