class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

        self.dic = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # print("GET", key)
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # print("PUT", key, value)
        if key in self.dic:
            self.remove(self.dic[key])
        
        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.tail.prev
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

    def add(self, node):
        node.prev = self.head
        next_head = self.head.next
        node.next = next_head
        next_head.prev = node
        self.head.next = node

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
