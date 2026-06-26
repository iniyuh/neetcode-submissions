class TreeNode:
    def __init__(self, key=0, val=0, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        if not self.root: self.root = TreeNode(key, val)
        else:
            curr = self.root
            while True:
                if curr.key < key: 
                    if curr.right: curr = curr.right
                    else: 
                        curr.right = TreeNode(key, val)
                        return
                elif key < curr.key:
                    if curr.left: curr = curr.left
                    else:
                        curr.left = TreeNode(key, val)
                        return
                else:
                    curr.val = val
                    return


    def get(self, key: int) -> int:
        curr = self.root

        while curr is not None:
            if curr.key < key: curr = curr.right
            elif key < curr.key: curr = curr.left
            else: return curr.val

        return -1

    def getMin(self) -> int:
        if not self.root: return -1

        curr = self.root
        while curr.left is not None: curr = curr.left
        return curr.val

    def getMax(self) -> int:
        if not self.root: return -1

        curr = self.root
        while curr.right is not None: curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def getInorderKeys(self, root: Optional[TreeNode]=None) -> List[int]:
        if root is None: 
            if self.root: root = self.root
            else: return []
        
        ret = []
        ret += self.getInorderKeys(root.left) if root.left else []
        ret += [root.key]
        ret += self.getInorderKeys(root.right) if root.right else []

        return ret


    def removeHelper(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root: return None

        if key < root.key: 
            root.left = self.removeHelper(root.left, key)
            return root
        elif root.key < key: 
            root.right = self.removeHelper(root.right, key)
            return root
        else:
            if not (root.left or root.right):
                return None
            elif not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                curr = root.right
                while curr.left: curr = curr.left
                root.right = self.removeHelper(root.right, curr.key)
                root.key, root.val = curr.key, curr.val
                return root
