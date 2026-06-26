class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjList[b].append(a)
        
        dependencies = defaultdict(set)
        visited = set()

        def dfs(target, course):
            if course in visited: return

            visited.add(course)
            dependencies[target].add(course)

            for pre in adjList[course]:
                dfs(target, pre)
            


        ret = []
        for a, b in queries:
            if b not in dependencies:
                visited.clear()
                dfs(b, b)
            ret.append(a in dependencies[b])
        
        return ret
