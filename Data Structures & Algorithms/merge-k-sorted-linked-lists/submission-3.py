# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []

        for i, listNode in enumerate(lists):
            heapq.heappush(minHeap, (listNode.val, i, listNode))
            lists[i] = lists[i].next
        
        rootNode = ListNode()
        currNode = rootNode

        while minHeap:
            _, index, nextNode = heapq.heappop(minHeap)

            if lists[index]: 
                heapq.heappush(minHeap, (lists[index].val, index, lists[index]))
                lists[index] = lists[index].next
            
            currNode.next = nextNode
            currNode = currNode.next
        
        return rootNode.next
        
