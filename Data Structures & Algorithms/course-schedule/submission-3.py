class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [[] for _ in range(numCourses)]        

        for i, j in prerequisites:
            courses[i].append(j)
        
        hist = set()

        def feasible(s, p):
            if not courses[p]: return True
            elif p in s: 
                return False
            else:
                if p in hist: return True

                s.add(p)
                for req in courses[p]:
                    if not feasible(s, req): return False
                
                hist.add(p)
                return True
        
        for prerequisiteList in courses:
            if prerequisiteList:
                for prerequisite in prerequisiteList:  
                    s = set()
                    if not feasible(s, prerequisite): return False
        
        return True
        