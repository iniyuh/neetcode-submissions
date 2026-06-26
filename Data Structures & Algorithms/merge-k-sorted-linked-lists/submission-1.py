# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode()
        listsEmpty = len(lists) == 0
        
        currentNode = head
        while not listsEmpty:
            listsEmpty = True

            # find list with min node exposed
            minVal, minIndex = float('inf'), None
            for i, list_ in enumerate(lists):
                if not list_: continue

                listsEmpty = False
                if list_.val < minVal:
                    minVal = list_.val
                    minIndex = i
            
            if not listsEmpty:
                print(minIndex, minVal)
                
                currentNode.next = lists[minIndex]
                lists[minIndex] = lists[minIndex].next
                # print(lists[minIndex].val)
                currentNode = currentNode.next
                currentNode.next = None

        return head.next

                
            



            