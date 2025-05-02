# Time Complexity O(N)
# Space Complexity O(N)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        if root == None:
            return root
        nodes_stack = [root]
        dummy_tree_node = TreeNode(0)
        dummy_node = dummy_tree_node
        while nodes_stack:
            poped_node = nodes_stack.pop()          
            if poped_node:
                left_node = poped_node.left
                right_node = poped_node.right
                nodes_stack.append(right_node)     
                nodes_stack.append(left_node)
            if poped_node:   
                new_node = TreeNode(poped_node.val)
                dummy_node.right = new_node
                dummy_node = dummy_node.right
        root.left = None
        root.right = None
        root.right = dummy_tree_node.right.right
      

       

        

                       
                        
                     
                        
                
                      
       
