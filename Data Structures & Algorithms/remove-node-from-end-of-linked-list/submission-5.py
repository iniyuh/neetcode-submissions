# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        L = 1
        prev = None

        while curr.next:

            if L == n + 1: prev = head

            curr = curr.next
            if prev: prev = prev.next
            L += 1
        
        if L == n + 1: prev = head
        
        if prev:
            print(prev.val, prev.next.val)
            prev.next = prev.next.next
            return head
        elif L == n: return head.next
        else: return head
        

           
