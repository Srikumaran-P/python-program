# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        temp=head
        curr=head.next
        prev=None
        while temp and temp.next:
            rizz=temp.next.next
            f=temp
            s=temp.next
            s.next=f
            f.next=rizz

            if prev:
                prev.next=s
            prev=f
            temp=rizz

        return curr
