class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # in order for it to not be possible to finish all courses
        # we must have the requirement to take some course BEFORE AND 
        # AFTER some other course

        # therefore we need to simply detect any cycle(s) in the dependency 
        # graphs of our courses 

        prereq = defaultdict(list)
        for a, b in prerequisites:
            prereq[a].append(b)


        visited = set()
        greenlit = set()
        def takeable(course):
            if course not in prereq: return True
            elif course in visited: return False
            else:
                visited.add(course)

                ret = True
                for pre in prereq[course]:
                    if not takeable(pre): 
                        ret = False
                        break
                
                greenlit.add(course)
                visited.remove(course)
                return ret
        
        for course in range(numCourses):
            if course not in greenlit and not takeable(course): return False
        
        return True

