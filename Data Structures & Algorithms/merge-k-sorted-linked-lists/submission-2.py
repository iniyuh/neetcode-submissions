# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()

        minHeap = []
        tiebreak = 0
        for list_ in lists:
            heapq.heappush(minHeap, (list_.val, tiebreak, list_))
            tiebreak += 1
        
        currentNode = head
        while minHeap:
            _, _, newNode = heapq.heappop(minHeap)

            currentNode.next = newNode
            currentNode = currentNode.next

            if currentNode.next:
                heapq.heappush(minHeap, (currentNode.next.val, tiebreak, currentNode.next))
                tiebreak += 1

        return head.next

                
            



            