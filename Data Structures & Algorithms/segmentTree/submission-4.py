class Node:
    def __init__(self, L: int, R: int, sum: int=0):
        self.L = L
        self.R = R
        self.sum = sum
        self.left = None
        self.right = None

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.root = self.build(0, len(nums) - 1)

    def build(self, L, R):
        if L == R: return Node(L, R, self.nums[L])
        else:
            ret = Node(L, R)
            M = (L + R) // 2
            ret.left = self.build(L, M)
            ret.right = self.build(M+1, R)
            ret.sum = ret.left.sum + ret.right.sum
            return ret

    
    def update(self, index: int, val: int, node: Node=None) -> None:
        if not node: node = self.root

        if node.L == node.R: node.sum = val
        else:
            M = (node.L + node.R) // 2
            if index <= M: 
                node.sum -= node.left.sum
                node.sum += self.update(index, val, node.left)
            else: 
                node.sum -= node.right.sum
                node.sum += self.update(index, val, node.right)
        
        return node.sum if node is not self.root else None
        
    
    def query(self, L: int, R: int, node: Node=None) -> int:
        if node == None: node = self.root

        if node.L == L and node.R == R: return node.sum
        else:
            M = (node.L + node.R) // 2

            if R <= M: return self.query(L, R, node.left)
            elif M < L: return self.query(L, R, node.right)
            else: return self.query(L, M, node.left) + self.query(M+1, R, node.right)

        



