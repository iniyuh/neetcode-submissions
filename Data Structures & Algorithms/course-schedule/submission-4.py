class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        hm = defaultdict(list)
        visited = set()

        for target, requisite in prerequisites:
            hm[target].append(requisite)

        def dfs(course):
            if course in visited: return False

            visited.add(course)
            for pre in hm[course]:
                if not dfs(pre): return False
            visited.remove(course)
            
            return True
        
        for course in range(numCourses):
            if not dfs(course): return False
        
        return True

