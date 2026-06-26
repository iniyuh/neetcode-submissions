class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        arr = [None] * numCourses
        mag = 0
        
        for i, j in prerequisites:
            if not arr[i]: arr[i] = [j]
            else: arr[i].append(j)
            mag += 1
        
        
        while True:
            prevMag = mag
        
            for i, adjList in enumerate(arr):
                if adjList:
                    for prereq in adjList:
                        if arr[prereq] == None: 
                            adjList.remove(prereq)
                            mag -= 1

                if not adjList: arr[i] = None
            
            if mag == prevMag: break
        
        return mag == 0
        