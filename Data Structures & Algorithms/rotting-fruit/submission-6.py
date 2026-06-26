class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def propogate(r, c):
            print("Propogate", r, c)
            res = []
            nonlocal visited

            if r+1 < len(grid) and grid[r+1][c] == 1 and (r+1, c) not in visited: 
                res.append((r+1, c))
                visited.add((r+1, c))
            if -1 < r-1 and grid[r-1][c] == 1 and (r-1, c) not in visited: 
                res.append((r-1, c))
                visited.add((r-1, c))
            if c+1 < len(grid[0]) and grid[r][c+1] == 1 and (r, c+1) not in visited: 
                res.append((r, c+1))
                visited.add((r, c+1))
            if -1 < c-1 and grid[r][c-1] == 1 and (r, c-1) not in visited: 
                res.append((r, c-1))
                visited.add((r, c-1))
            return res



        currentRottens = []
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2: 
                    currentRottens.append((r, c))
                    visited.add((r,c ))
                elif grid[r][c] == 0:
                    visited.add((r, c))
        timeStamp = 0

        while currentRottens:
            newRottens = []
            for r, c in currentRottens:
                newRottens += propogate(r, c)
            
            if newRottens: timeStamp += 1
            currentRottens = newRottens
        
        print(visited)
        return timeStamp if len(visited) == len(grid) * len(grid[0]) else -1