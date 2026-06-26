class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for a, b in prerequisites:
            prereq[a].append(b)
        print(prereq)
        
        accounted = set()
        visited = set()
        ret = []
        def dfs(course):
            if course in visited: return False
            elif course in accounted: return True
            elif course not in prereq:
                ret.append(course)
                accounted.add(course)
                return True
            else:
                accounted.add(course)
                visited.add(course)

                for pre in prereq[course]:
                    if not dfs(pre): return False

                visited.remove(course)
                ret.append(course)
                return True
        
        for course in range(numCourses):
            # if not dfs(course): return []
            val = dfs(course)
            print(course, val)
            if not val: return []
            # visited.clear()
        
        return ret
                
        


