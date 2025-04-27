class Solution(object):
    def setZeroes(self, matrix):
        lines0 = set()
        columns0 = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    lines0.add(i)
                    columns0.add(j)

        for i in lines0:
            for j in range(len(matrix[0])) :
                matrix[i][j] = 0
        for j in columns0:
            for i in range(len(matrix)):
                matrix[i][j] = 0
