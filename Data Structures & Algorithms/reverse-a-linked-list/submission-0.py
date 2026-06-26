# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        next_ = head.next

        while next_:
            curr.next = prev
            prev = curr
            curr = next_
            next_ = next_.next
        
        curr.next = prev
        return curr
            