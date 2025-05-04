"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        # pointer to orig
        orig = head
        # deep copy
        anchor = Node(0)
        curr = anchor
        # create mapping
        node_map = {}
        while orig:             
            
            # add immediately to node_map
            if orig not in node_map:
                node_map[orig] = Node(orig.val)         
            if orig.next and orig.next not in node_map:
                node_map[orig.next] = Node(orig.next.val)
            if orig.random and orig.random not in node_map:
                node_map[orig.random] = Node(orig.random.val)

            # retrieve copies from node_map
            orig_cpy = node_map[orig]
            next_cpy = node_map[orig.next] if orig.next else None
            rand_cpy = node_map[orig.random] if orig.random else None

            # link the current deep copy node
            curr.next = orig_cpy
            curr.next.next = next_cpy
            curr.next.random = rand_cpy

            # advance pointers
            orig = orig.next
            curr = curr.next

        return anchor.next
                
