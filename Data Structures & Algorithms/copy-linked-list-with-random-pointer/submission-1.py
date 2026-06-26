"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ret = None
        
        prev = None
        curr = head
        hm = {}
        waitlist = defaultdict(list)

        while curr:
            new_node = Node(curr.val)
            hm[curr] = new_node

            if curr.random:
                if curr.random not in hm: 
                    waitlist[curr.random].append(new_node)
                else: new_node.random = hm[curr.random]
            
            if curr in waitlist:
                for waiting_node in waitlist[curr]:
                    waiting_node.random = new_node
                del waitlist[curr]
            

            if not ret: ret = new_node
            else: prev.next = new_node
            prev = new_node
            curr = curr.next
            
        
        return ret
            