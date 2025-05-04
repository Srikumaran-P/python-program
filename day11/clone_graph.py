"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
       
        if not node:
            return None

    
        
        q = []
        
        
        q.append(node)

        
        cloned_node = Node(node.val)

        mapping = {node: cloned_node}

        while q:
            currentNode = q.pop(0)  

            for vicino in currentNode.neighbors:
                if vicino not in mapping:
                    cloned_vicino = Node(vicino.val)
                    mapping[vicino] = cloned_vicino  
                    q.append(vicino)

                
                mapping[currentNode].neighbors.append(mapping[vicino])

        return cloned_node



        
