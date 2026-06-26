class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        memo = {}
        visited = set()
        len_r, len_c = len(heights), len(heights[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def arrayOr(arr1, arr2):
            for i in range(len(arr1)):
                arr1[i] |= arr2[i]

        def calc(r, c):
            if (r, c) in memo: return memo[(r, c)]
            else:
                visited.add((r, c))
                res = [0, 0]
                myHeight = heights[r][c]

                if r  == 0 or c == 0: res[0] |= 1
                if r + 1 == len_r or c + 1 == len_c: res[1] |= 1
                
                i = 0
                for dr, dc in directions:
                    if res == [1, 1]: break
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < len_r and 0 <= nc < len_c and heights[nr][nc] <= myHeight and (nr, nc) not in visited:
                        arrayOr(res, calc(nr, nc))
                
                memo[(r, c)] = res
                visited.remove((r,c))
                return res
        

        answer = []
        for r in range(len_r):
            for c in range(len_c):
                if calc(r, c) == [1, 1]: answer.append([r, c])
        
        return answer


