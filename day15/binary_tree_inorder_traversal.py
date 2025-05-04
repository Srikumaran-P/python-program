# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        l=[]
        def itr(root):
            if root==None:return 
            itr(root.left)
            l.append(root.val)
            itr(root.right)
        itr(root)
        return l   
        
