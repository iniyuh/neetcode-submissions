# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        elif not list2: return list1

        a, b = (list1, list2) if list1.val < list2.val else (list2, list1)
        root = curr = a
        a = a.next

        while a:
            if not b: 
                curr.next = a
                curr = curr.next
                a = a.next
            else:
                if a.val < b.val:
                    curr.next = a
                    curr = curr.next
                    a = a.next
                else:
                    curr.next = b
                    curr = curr.next
                    b = b.next

        while b:
            curr.next = b
            curr = curr.next
            b = b.next
        
        return root