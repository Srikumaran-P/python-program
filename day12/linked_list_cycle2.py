class Solution(object):
    def detectCycle(self, head):
        fast = head
        slow = head
        while fast and fast.next:
              fast = fast.next.next
              slow = slow.next
              if fast==slow:
                 fast = head
                 while fast!=slow:
                    fast = fast.next
                    slow = slow.next
                 return fast
        return None
