# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: return None
        
        return self.partition(lists, 0, len(lists) - 1)

    def partition(self, lists, l, r):
        if l == r: return lists[l]

        m = l + ((r - l) // 2)

        left = self.partition(lists, l, m)
        right = self.partition(lists, m+1, r)

        return self.merge(left, right)
    
    def merge(self, list_a, list_b):
        root = ListNode(None)
        curr = root

        while list_a and list_b:
            if list_a.val <= list_b.val:
                curr.next = list_a
                curr = curr.next
                list_a = list_a.next
            else:
                curr.next = list_b
                curr = curr.next
                list_b = list_b.next
        
        if list_a: curr.next = list_a
        if list_b: curr.next = list_b

        return root.next
