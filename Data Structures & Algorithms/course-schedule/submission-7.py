class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjList[a].append(b)

        visited = set()
        cycle = set()

        def dfs(course):
            if course in cycle: return False
            elif course in visited: return True

            visited.add(course)
            cycle.add(course)

            for prereq in adjList[course]:
                if not dfs(prereq): return False
            
            cycle.remove(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        return True

