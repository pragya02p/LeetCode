# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """if root==None:
            return []
        return self.inorderTraversal(root.left)+ [root.val]+self.inorderTraversal(root.right)
        """
        if root==None:
            return []
        stack=[]
        curr=root
        l=[]
    
        while curr!=None or stack!=[]:
            if curr!=None:
                stack.append(curr)
                curr=curr.left
            else:
                curr=stack.pop()
                l.append(curr.val)
                curr=curr.right
            
        return l
        