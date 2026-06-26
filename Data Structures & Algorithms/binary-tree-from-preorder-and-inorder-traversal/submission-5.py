# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
            
        def helper(preorder_start, preorder_end, inorder_start, inorder_end):
            root_value = preorder[preorder_start]
            root_index_inorder = inorder.index(root_value)
            left_tree_length = root_index_inorder - inorder_start
            right_tree_length = inorder_end - inorder_start - root_index_inorder - 1

            root_node = TreeNode(root_value)
            root_node.left = self.buildTree(preorder[preorder_start+1:preorder_start+1+left_tree_length], inorder[inorder_start:root_index_inorder]) if left_tree_length > 0 else None
            root_node.right = self.buildTree(preorder[preorder_start+1+left_tree_length:preorder_end], inorder[root_index_inorder+1:inorder_end]) if right_tree_length > 0 else None

            return root_node
        
        return helper(0, len(preorder), 0, len(inorder))