class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # for each course
            # check if there is any way to take said course
            # if so, store that pathway and mark all courses
            # in the pathway as complete
        
        pre = defaultdict(list)
        taken = set()
        visited = set()
        ret = []


        for a, b in prerequisites:
            pre[a].append(b)

        def dfs(course):
            if course in visited: return False
            elif course in taken: return True
            else:
                visited.add(course)

                for prereq in pre[course]:
                    if not dfs(prereq): return False
                
                visited.remove(course)
                taken.add(course)
                ret.append(course)
                return True


                



        for course in range(numCourses):
            if not dfs(course): return []
        
        return ret

        
