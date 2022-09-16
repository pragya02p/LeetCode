# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is  None:
            return False
        q=[root]
        p=[root.val]
        
        while len(q)>0:
            t=q.pop(0)
            pathsum=p.pop(0)
            print(pathsum)
            if t.left==None and t.right==None:
                if pathsum==targetSum:
                    return True
            if t.left:
                q.append(t.left)
                p.append(pathsum+t.left.val)
            if t.right:
                q.append(t.right)
                p.append(pathsum+t.right.val)
            
        return False
                    