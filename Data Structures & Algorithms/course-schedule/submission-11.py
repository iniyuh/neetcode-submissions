class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for post, pre in prerequisites:
            adjList[post].append(pre)
        
        visited = set()
        cycle = set()
        
        def kahns(course):
            if course in cycle: return False
            elif course in visited: return True
            else:
                cycle.add(course)
                visited.add(course)

                for pre in adjList[course]:
                    if not kahns(pre): 
                        cycle.remove(course)
                        return False

                cycle.remove(course)
                return True
        
        for course in range(numCourses):
            if not kahns(course): return False
        
        return True
