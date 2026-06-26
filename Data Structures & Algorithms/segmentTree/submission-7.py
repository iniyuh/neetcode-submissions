class Node:
    def __init__(self, L, R, sum=0):
        self.L = L
        self.R = R
        self.left = None
        self.right = None
        self.sum = sum

class SegmentTree:
    @staticmethod
    def build(L, R, nums):
        if L == R: return Node(L, R, nums[L])

        node = Node(L, R)
        M = (L + R) // 2
        node.left = SegmentTree.build(L, M, nums)
        node.right = SegmentTree.build(M+1, R, nums)

        node.sum = node.left.sum + node.right.sum

        return node

    
    def __init__(self, nums: List[int]):
        self.root = SegmentTree.build(0, len(nums) - 1, nums)
    
    def update(self, index: int, val: int, node: Node = None) -> None:
        if not node: node = self.root
        
        if node.L == node.R: 
            node.sum = val
        else:
            M = (node.L + node.R) // 2

            if index <= M: self.update(index, val, node.left)
            else: self.update(index, val, node.right)

            node.sum = node.left.sum + node.right.sum
    
    def query(self, L: int, R: int, node: Node = None) -> int:
        if node is None: 
            print("----------")
            node = self.root

        print(L, R, node.L, node.R)

        if node.L == L and node.R == R: 
            print("BANG")
            return node.sum
        else:
            M = (node.L + node.R) // 2
            ret = 0

            if L <= M: ret += self.query(L, min(M, R), node.left)
            if M < R: ret += self.query(max(L, M+1), R, node.right)

            return ret
            

