# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
two passes
first to calculate length
second to remove node
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        secondLast = None
        node = head

        while node.next:
            length += 1
            secondLast = node
            node = node.next
        
        length += 1
        

        targetIndex = length - n

        if targetIndex == 0:
            temp = head.next
            head.next = None

            return temp
        elif n == 1:
            secondLast.next = None
            return head
        

        i = 0
        predecessor = head
        while predecessor:
            if i == targetIndex - 1:
                target = predecessor.next
                successor = target.next
                target.next = None

                predecessor.next = successor
                
                return head
            else:
                predecessor = predecessor.next
                i += 1
