class TreeNode:
    def __init__(self, l, r, val=None):
        self.l = l
        self.r = r
        
        self.val = val

        self.left = None
        self.right = None

class SegmentTree:
    @staticmethod
    def build(l, r, nums):
        if l == r: return TreeNode(l, r, nums[l])

        curr = TreeNode(l, r)
        M = (l + r) // 2

        curr.left = SegmentTree.build(l, M, nums)
        curr.right = SegmentTree.build(M+1, r, nums)

        curr.val = curr.left.val + curr.right.val

        return curr

    def __init__(self, nums: List[int]):
        self.root = self.build(0, len(nums) - 1, nums)
    
    def update(self, index: int, val: int, curr: TreeNode=None) -> None:
        if not curr: curr = self.root
        
        if curr.l == curr.r: curr.val = val
        else:
            M = (curr.l + curr.r) //2

            if index <= M: 
                curr.val -= curr.left.val
                curr.val += self.update(index, val, curr.left)
            else: 
                curr.val -= curr.right.val
                curr.val += self.update(index, val, curr.right)
        
        return curr.val if curr is not self.root else None
    
    def query(self, L: int, R: int, curr: TreeNode=None) -> int:
        if not curr: curr = self.root
        
        M = (curr.l + curr.r) // 2

        if curr.l == L and curr.r == R: return curr.val
        elif R <= M: return self.query(L, R, curr.left)
        elif M < L: return self.query(L, R, curr.right)
        else: return self.query(L, M, curr.left) + self.query(M+1, R, curr.right)






