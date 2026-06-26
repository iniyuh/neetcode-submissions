class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = defaultdict(list)
        for crs, pre in prerequisites:
            prereq[crs].append(pre)
        
        cycle, visited = set(), set()
        ret = []

        def dfs(crs):
            if crs in cycle: return False
            if crs in visited: return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            visited.add(crs)
            ret.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return []
        
        return ret