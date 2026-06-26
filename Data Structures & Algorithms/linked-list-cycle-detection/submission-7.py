# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        We can use a slow and fast pointer to detect a cycle
        """
        if not head: return False

        slow, fast = head, head
        while True:
            slow = slow.next
            fast = fast.next
            if not fast or not fast.next: return False
            fast = fast.next

            if slow == fast: return True