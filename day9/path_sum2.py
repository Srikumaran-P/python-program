# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
            
        return self.get_sum(root, targetSum, [])


    def get_sum(self, root, target, cur_path):
        left_child, right_child = root.left, root.right

        if left_child is None and right_child is None:
            cur_path += [root.val]

            if sum(cur_path) == target:
                return [cur_path]
            return []
        
        if left_child:
            left_path = self.get_sum(root.left, target, cur_path+[root.val])
        else:
            left_path = []
        if right_child:
            right_path = self.get_sum(root.right, target, cur_path+[root.val])
        else:
            right_path = []

        return right_path + left_path
