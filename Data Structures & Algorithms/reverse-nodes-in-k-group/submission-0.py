# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head

            temp = curr
            for _ in range(k): 
                if not temp: return 0, 0, 0
                temp = temp.next

            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            h = prev
            t = head
            t.next = curr

            return h, t, t.next

        length = 1
        curr = head
        ret = None

        while curr:
            if not ret:
                h, t, after = reverse(curr)
                ret = h
                curr = t
            elif curr.next:
                h, t, after = reverse(curr.next)

                if h == t == after == 0: break

                curr.next = h
                curr = t
            else: break
        
        return ret