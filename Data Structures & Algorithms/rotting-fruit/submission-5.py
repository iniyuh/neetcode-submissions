class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        len1, len2 = len(grid), len(grid[0])

        checklist = set()
        q = collections.deque()
        for i in range(len1):
            for j in range(len2):
                if grid[i][j] == 1:
                    checklist.add((i, j)) 
                elif grid[i][j] == 2:
                    q.append((i, j))
        print("Checklist", checklist)
        print("Starting points", q)

        if not checklist: return 0
        
        timestamp = 0
        for i, j in q:
            grid[i][j] = 0
        directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
        
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()

                checklist.discard((i, j))
                if not checklist: return timestamp

                for direction in directions:
                    i_, j_ = i + direction[0], j + direction[1]
                    if not (
                        i_ < 0 or
                        j_ < 0 or
                        len1 <= i_ or
                        len2 <= j_ or
                        grid[i_][j_] == 0
                    ):
                        grid[i_][j_] = 0
                        q.append((i_, j_))

            
            timestamp += 1
        
        return -1

