class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:        
        words_length = len(words)
        word_lengths = [len(word) for word in words]

        R, C = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        # O(m) where m is number of words
        def vibeCheck(currentString):
            length = len(currentString)
            for i in range(words_length):
                if currentString == words[i][0 : length]:
                    if length == word_lengths[i]: return "HIT"
                    else: return "PROCEED"
            return "MISS"
        
        def explore(currentString, r, c):
            currentString += board[r][c]

            nonlocal visited
            visited.add((r, c))
            for dr, dc in directions:
                dfs(currentString, r + dr, c + dc)
            visited.remove((r, c))
        
        def dfs(currentString, r, c):
            if (r, c) in visited or r < 0 or c < 0 or r == R or c == C: return
            else:
                match vibeCheck(currentString + board[r][c]):
                    case "HIT":
                        nonlocal res
                        res.add(currentString + board[r][c])

                        explore(currentString, r, c)
                    case "PROCEED":
                        explore(currentString, r, c)
                    case "MISS":
                        return

        
        res = set()
        visited = set()
        
        for r in range(R):
            for c in range(C):
                dfs("", r, c)
        
        print(res)
        return list(res)
        

        
        