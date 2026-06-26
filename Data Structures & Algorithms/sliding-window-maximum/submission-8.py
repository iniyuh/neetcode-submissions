class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        maxHeap = []
        popHeap = []
        ret = []

        for r in range(len(nums)):
            # load
            if r < k:
                heapq.heappush(maxHeap, -1 * nums[r])

                if r == k - 1: ret.append(-1 * maxHeap[0])
            
            # window at size
            else:
                # alters max
                if nums[l] == -1 * maxHeap[0]:
                    heapq.heappop(maxHeap)

                    while popHeap and popHeap[0] == maxHeap[0]:
                        heapq.heappop(popHeap)
                        heapq.heappop(maxHeap)
                else:
                    # stash for deletion later
                    heapq.heappush(popHeap, -1 * nums[l])
                
                l += 1

                heapq.heappush(maxHeap, -1 * nums[r])

                ret.append(-1 * maxHeap[0])
        
        return ret
                

