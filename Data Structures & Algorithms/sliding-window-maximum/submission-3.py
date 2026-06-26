class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap, res = [], []
        for i in range(len(nums)):
            if i < k - 1:
                heapq.heappush(heap, (-1 * nums[i], i))
            else:
                while heap and heap[0][1] < i - k + 1:
                    heapq.heappop(heap)
                
                heapq.heappush(heap, (-1 * nums[i], i))
                res.append(heap[0][0] * -1)
        return res

