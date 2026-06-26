class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjList[a].append(b)

        path = []
        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle: return False
            elif course in visited: return True

            cycle.add(course)

            for pre in adjList[course]:
                if not dfs(pre): return False

            cycle.remove(course)
            visited.add(course)
            path.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course): return []
        
        return path
