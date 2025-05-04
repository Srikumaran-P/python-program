class Solution(object):
    def reorderList(self, head):
        def rev_list(head):
            hold = None
            while head:
                t = head.next
                head.next = hold
                hold = head
                head = t
            return hold
        def find_mid(head):
            fast = head
            slow = head
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            return slow
        m = find_mid(head)
        sec = rev_list(m.next)
        temp = head
        while sec:
           t = temp.next
           temp.next = sec
           sec = sec.next
           temp.next.next = t
           temp = t
        m.next = None
        return head
