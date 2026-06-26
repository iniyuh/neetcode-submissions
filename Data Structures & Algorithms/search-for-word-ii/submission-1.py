class TrieNode:
    def __init__(self):
        self.hm = {}
        self.isWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Setup word trie
        trie = TrieNode()
        for word in words:
            currNode = trie
            for char in word:
                if char not in currNode.hm: currNode.hm[char] = TrieNode()
                currNode = currNode.hm[char]
            currNode.isWord = True
        

        R, C = len(board), len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1)]


        
        # DFS
        def dfs(r, c, currNode, currString):
            nonlocal visited

            if r < 0 or c < 0 or r == R or c == C or (r,c) in visited: return False
            elif board[r][c] not in currNode.hm: return False
            else:
                currNode = currNode.hm[board[r][c]]
                currString += board[r][c]

                if currNode.isWord: 
                    nonlocal solution
                    solution.add(currString)

                visited.add((r, c))

                for dr, dc in directions:
                    dfs(r + dr, c + dc, currNode, currString)

                visited.remove((r,c))
        






        visited = set()
        solution = set()
        for r in range(R):
            for c in range(C):
                dfs(r, c, trie, "")

        return list(solution)
        


        
