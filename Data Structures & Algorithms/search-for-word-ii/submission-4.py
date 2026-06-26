class Node:
    def __init__(self):
        self.hm = {}
        self.isWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        
        root = Node()
        visited = set()
        ret = set()

        def explore(node, r, c, string):

            if (r,c) in visited or r <= -1 or c <= -1 or r >= R or c >= C or board[r][c] not in node.hm: 
                return
            else:
                visited.add((r,c))
                
                string += board[r][c]

                new_node = node.hm[board[r][c]]

                if new_node.isWord: ret.add(string)

                for dr, dc in directions:
                    explore(new_node, r+dr, c+dc, string)
                visited.remove((r,c))


        # mark words in trie:
        for word in words:
            node = root
            for char in word:
                if char not in node.hm: node.hm[char] = Node()
                node = node.hm[char]
            node.isWord = True

        # create trie
        for r in range(R):
            for c in range(C):
                explore(root, r, c, "")

        return list(ret)