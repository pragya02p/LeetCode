# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []
        """
        if root==None:
            return []
        curr=root
        right_node=[]
        main_node=[]
        l=[]
        while curr or len(main_node)>0:
            if curr!=None:
                if curr.right!=None:
                    right_node.append(curr.right)
                main_node.append(curr)
                curr=curr.left
            else:
                curr=main_node[len(main_node)-1]
                if right_node!=[] and curr.right==right_node[len(right_node)-1] :
                    curr=right_node.pop()
                else:
                    l.append(curr.val)
                    main_node.pop()
                    curr=None
                    
                    
        return l
                
        
        