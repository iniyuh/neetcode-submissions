# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: return ""
        
        ret = ""
        q = deque()
        q.append(root)

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if not node: ret += "null,"
                else:
                    ret += str(node.val)
                    ret += ","
                    q.append(node.left)
                    q.append(node.right)
        
        return ret

        
    def helper(self, string, idx):
        i = idx

        while string[i] != ",": i += 1
        if string[idx:i] == "null":
            return (None, i+1)
        else:
            return (int(string[idx:i]), i+1)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "": return None

        idx = 0

        val, idx = self.helper(data, idx)
        if not val: return None
        rootNode = TreeNode(val)
        q = deque()
        q.append(rootNode)

        while idx != len(data):
            node = q.popleft()

            leftVal, idx = self.helper(data, idx)
            if leftVal: 
                node.left = TreeNode(leftVal)
                q.append(node.left)
            
            rightVal, idx = self.helper(data, idx)
            if rightVal: 
                node.right = TreeNode(rightVal)
                q.append(node.right)
        
        return rootNode


        

