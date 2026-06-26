class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    
    def find(self, i):
        if self.par[i] == i: return i
        else:
            self.par[i] = self.find(par[i])
            return self.par[i]
    
    def union(self, i, j):
        a, b = self.find(i), self.find(j)

        if a == b: return False

        if self.rank[a] == self.rank[b]:
            self.rank[a] += 1
            self.par[b] = a
        elif self.rank[a] < self.rank[b]:
            self.par[a] = b
        else:
            self.par[b] = a

        return True


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i]
            for j in range(len(points)):
                if i == j: continue

                xj, yj = points[j]

                adjList[i].append((abs(xi - xj) + abs(yi - yj), j))

        minHeap = [(0, 0)]
        visited = set()
        cost = 0

        while len(visited) != len(points):
            dist, point = heapq.heappop(minHeap)

            if point in visited: continue

            cost += dist
            visited.add(point)

            for item in adjList[point]: heapq.heappush(minHeap, item)
        
        return cost


        