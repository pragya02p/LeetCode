# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        node=TreeNode()
        def merge_root(t1,t2):
            if t1==None:
                return t2
            if t2==None:
                return t1
            t1.val+=t2.val
            t1.left=merge_root(t1.left,t2.left)
            t1.right=merge_root(t1.right,t2.right)
            return t1
        root3=merge_root(root1,root2)
        return root3
        
        
        