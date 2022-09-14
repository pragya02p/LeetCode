# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root==None:
            return []
        l=[root]
        t=[]
        tl=[root.val]
        
        while True:
            nodecount=len(l)
            if nodecount==0:
                return t
            t.append(tl)
            tl=[]
            while nodecount>0:
                node=l.pop(0)
                
                if node.left!=None:
                    l.append(node.left)
                    tl.append(node.left.val)
                    
                if node.right!=None:
                    l.append(node.right)
                    tl.append(node.right.val)
                    
                nodecount-=1
        return t
        
        