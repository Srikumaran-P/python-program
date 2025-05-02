# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def dfs(self , root , res , targetSum , ans ):
        if not root:
            return None
        
        res += root.val 

        if not root.left and not root.right:
            if res == targetSum:
                ans[0] = True
                return
            else:
                res -= root.val
        
        
        if root.left:
            self.dfs(root.left , res , targetSum ,ans)
        if root.right:
            self.dfs(root.right , res , targetSum , ans)
        
        # return False


    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """

        if not root:
            return False 
        res = 0
        ans = [False]

        self.dfs(root , res , targetSum , ans)
        return  ans[0]

        
