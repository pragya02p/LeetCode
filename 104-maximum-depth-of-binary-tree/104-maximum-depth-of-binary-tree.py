# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root ==None:
            return 0
        l=[root]
        h=0
        while True:
            nodecount=len(l)
            if nodecount==0:
                return h
            h+=1
            while nodecount>0:
                q=l.pop(0)
                if q.left!=None:
                    l.append(q.left)
                if q.right!=None:
                    l.append(q.right)
                nodecount-=1
        return h
        