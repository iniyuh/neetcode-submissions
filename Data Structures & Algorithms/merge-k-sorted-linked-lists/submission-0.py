# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def _lt(self, other):
    return self.val < other.val

ListNode.__lt__ = _lt

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        for node in lists:
            heapq.heappush(minHeap, node)

        head = ListNode(0)
        curr = head
        
        while minHeap:
            node = heapq.heappop(minHeap)

            while node and ((node.val <= minHeap[0].val) if minHeap else True):
                curr.next = node
                curr = node
                node = node.next
            
            if node: heapq.heappush(minHeap, node)
        
        return head.next

