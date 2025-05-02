# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self, root, temp, pre, unright1, unright2):
        if not root:
            return
        self.inorder(root.left, temp, pre, unright1, unright2)
        temp.append(root.val)
        if pre[0] and root.val < pre[0].val:
            if not unright1[0]:
                unright1[0] = pre[0]
            unright2[0] = root
        pre[0] = root
        self.inorder(root.right, temp, pre, unright1, unright2)

    def recoverTree(self, root):
        unright1 = [None]
        unright2 = [None]
        pre = [None]
        self.inorder(root, [], pre, unright1, unright2)
        if unright1[0] and unright2[0]:
            unright1[0].val, unright2[0].val = unright2[0].val, unright1[0].val
        return root

        
