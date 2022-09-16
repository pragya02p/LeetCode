# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return root
        q=[root]
        while len(q)>0:
            t=q.pop(0)
            v=t.left
            t.left=t.right
            t.right=v
            if t.left:
                q.append(t.left)
            if  t.right:
                q.append(t.right)
            
        return root
        