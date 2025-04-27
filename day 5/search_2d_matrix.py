class Solution(object):
    def searchMatrix(self, matrix, target):
        arr = []
        for i in matrix:
            arr += i
        return target in arr
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
