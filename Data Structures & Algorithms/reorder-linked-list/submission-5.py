# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head.next: return

        prev = None
        slow, fast = head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        prev = None
        head2 = slow
        while head2:
            temp = head2.next
            head2.next = prev
            prev = head2
            head2 = temp
        
        head2 = prev
        head1 = head
        while head1.next:
            next1 = head1.next
            next2 = head2.next

            head1.next = head2
            head2.next = next1
            # next1.next = next2

            head1 = next1
            head2 = next2
        
        head1.next = head2

        return
        
        