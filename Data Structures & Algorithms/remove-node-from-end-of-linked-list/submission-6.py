# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
array and then omit using length of array and node pointers
"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        node = head
        while node:
            arr.append(node)
            node = node.next
        
        target = len(arr) - n

        if target == 0:
            temp = head.next
            head.next = None
            return temp
        elif n == 1:
            arr[-2].next = None
            return head
        else:
            temp = arr[target].next
            arr[target].next = None

            arr[target - 1].next = temp
            return head