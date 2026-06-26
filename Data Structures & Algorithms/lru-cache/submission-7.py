class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hm = {}

        self.left = Node("!", 0)
        self.right = Node("!", 0)
        self.left.right = self.right
        self.right.left = self.left

    def get(self, key: int) -> int:
        if key in self.hm: 
            node = self.hm[key]

            node.left.right = node.right
            node.right.left = node.left

            node.left = self.right.left
            node.right = self.right
            self.right.left.right = node
            self.right.left = node

            return node.val
        else: return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.hm:
            new_node = Node(key, value)

            if len(self.hm) == self.capacity:
                del self.hm[self.left.right.key]

                self.left.right = self.left.right.right
                self.left.right.left = self.left

            self.hm[key] = new_node

            new_node.left = self.right.left
            new_node.right = self.right
            self.right.left.right = new_node
            self.right.left = new_node

        else:
            node = self.hm[key]
            node.val = value

            node.left.right = node.right
            node.right.left = node.left

            node.left = self.right.left
            node.right = self.right
            self.right.left.right = node
            self.right.left = node

                


        
