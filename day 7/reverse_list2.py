# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        node = head
        hold = []
        i = 0
        l = left -1
        r = right -1

        while node:
            hold.append(node.val)
            node = node.next
        
        while l < r:
            hold[l],hold[r] = hold[r],hold[l]
            l += 1
            r -= 1
        
        tmp = node = ListNode(-1)
        
        for n in hold:
            tmp.next = ListNode(n)
            tmp = tmp.next
        
        return node.next
