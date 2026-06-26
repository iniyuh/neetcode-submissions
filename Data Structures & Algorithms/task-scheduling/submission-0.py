class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        bucket = [0] * 26

        for task in tasks:
            bucket[ord(task) - ord("A")] += 1
        
        maxHeap = []

        for count in bucket: 
            if count != 0: maxHeap.append(-1 * count)
        heapq.heapify(maxHeap)
        q = deque()
        timestamp = 0

        while maxHeap or q:
            if not maxHeap: timestamp = q[0][0]

            while q and timestamp >= q[0][0]: heapq.heappush(maxHeap, -1 * q.popleft()[1])

            count = -1 * heapq.heappop(maxHeap)
            count -= 1

            if count != 0: q.append((timestamp + n + 1, count))
            
            timestamp += 1
        
        return timestamp
