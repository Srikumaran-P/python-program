# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sub(self, l):
        if len(l) == 0:
            return None
        mid = len(l) // 2
        root = TreeNode(l[mid])
        root.left = self.sub(l[:mid])
        root.right = self.sub(l[mid + 1:])
        return root
    def sortedListToBST(self, head):
        l = []
        while head:
            l.append(head.val)
            head = head.next
        return self.sub(l)
        

        
