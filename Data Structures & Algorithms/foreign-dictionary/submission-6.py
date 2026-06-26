class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adjList = defaultdict(list)

        def updateAdjList(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]: i += 1

            if i == len(a): return True

            if i == len(b): return False
        
            adjList[a[i]].append(b[i])
            return True

        
        for i in range(len(words) - 1): 
            if not updateAdjList(words[i], words[i+1]): return ''

        ret = []
        visited = set()
        letters = set()

        for word in words:
            for char in word: letters.add(char)


        def dfs(u, cycle):
            if u in cycle: return False
            if u in visited: return True

            cycle.add(u)

            for v in adjList[u]:
                if not dfs(v, cycle): return False
            
            cycle.remove(u)
            visited.add(u)
            ret.append(u)

            return True

        
        for letter in letters:
            cycle = set()
            if not dfs(letter, cycle): return ""

        ret.reverse()
        return "".join(ret)
