# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        maxDepth = -1
        currDepth = 0
        visited = set()
        path = []
        curr = root
        ret = []

        while curr:
            # print("Path:", [x.val for x in path], ". Visiting", curr.val)
            print("Visiting", curr.val, "currDepth", currDepth)
            visited.add(curr)

            if currDepth > maxDepth: 
                ret.append(curr.val)
                maxDepth = currDepth
                # print("Added", curr.val, "maxdepth", maxDepth)

            if curr.right not in visited and curr.right: 
                path.append(curr)
                curr = curr.right
                currDepth += 1
            elif curr.left not in visited and curr.left:
                path.append(curr)
                curr = curr.left
                currDepth += 1
            else:
                if not path: break

                curr = path[-1]
                path.pop()
                currDepth -= 1
        
        return ret

            