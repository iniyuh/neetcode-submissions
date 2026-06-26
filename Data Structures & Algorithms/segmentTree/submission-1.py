class SegmentNode:

    def __init__(self, L, R, sum=0):
        self.L = L
        self.R = R
        self.sum = sum

        self.left = None
        self.right = None

class SegmentTree:
    @staticmethod
    def build(nums, L, R):
        if L == R: 
            # print(L, "to", R, "sum =", nums[L])
            return SegmentNode(L, R, nums[L])

        ret = SegmentNode(L, R)
        M = (L + R) // 2
        ret.left = SegmentTree.build(nums, L, M)
        ret.right = SegmentTree.build(nums, M+1, R)
        ret.sum = ret.left.sum + ret.right.sum
        # print(L, "to", R, "sum =", ret.sum)
        return ret

    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)
    
    def update(self, index: int, val: int, node: SegmentNode = None) -> None:
        # return None
        if not node: node = self.root
        
        ret = 0
        M = (node.L + node.R) // 2

        if node.L == index == node.R: 
            node.sum = val
            ret =  val
        elif index <= M:
            node.sum -= node.left.sum
            node.sum += self.update(index, val, node.left)
            ret = node.sum
        elif M < index:
            node.sum -= node.right.sum
            node.sum += self.update(index, val, node.right)
            ret = node.sum

        return ret if node is not self.root else None
    
    def query(self, L: int, R: int, node: SegmentNode = None) -> int:
        if not node: node = self.root

        if node.L == L and node.R == R: return node.sum
        else:
            M = (node.L + node.R) // 2

            if R <= M: return self.query(L, R, node.left)
            elif M < L: return self.query(L, R, node.right)
            else: return self.query(L, M, node.left) + self.query(M+1, R, node.right)
