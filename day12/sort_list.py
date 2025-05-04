# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        ans=[]
        curr=head
        i=0
        while curr:
            ans.append(curr.val)
            i+=1
            curr=curr.next

        ans.sort()

        cur=head
        j=0
        while cur:
            cur.val=ans[j]
            j+=1
            cur=cur.next

        return head    




        
            


        
