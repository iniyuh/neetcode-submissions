class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            adjList[a].append(b)
    
        visited = set()

        def canComplete(course):
            if course in visited: return False
            elif not adjList[course]: return True
            else:
                visited.add(course)

                for prereq in adjList[course]:
                    if not canComplete(prereq): 
                        visited.remove(course)
                        return False
                
                visited.remove(course)
                return True
                


        

        for course in range(numCourses):
            if not canComplete(course): return False
        
        return True


        