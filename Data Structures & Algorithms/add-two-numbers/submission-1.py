# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None
        carry = 0

        while l1 or l2:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            digit = val % 10
            carry = val // 10

            new_node = ListNode(digit)

            if not head: 
                head = new_node
                prev = head
            else:
                prev.next = new_node
                prev = new_node
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        if carry != 0:
            prev.next = ListNode(carry)
        
        return head


