class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n, m = len(matrix), len(matrix[0])
        checked = [[False for _ in range(m)] for _ in range(n)]
        result = []
        r, c = 0, 0
        go_dir = [0, 1] # go right
        while(True):
            v = matrix[r][c]
            checked[r][c] = True
            result.append(v)

            right = r < n and (c+1) < m and not checked[r][c+1]
            down = (r+1) < n and c < m and not checked[r+1][c]
            left = r >= 0 and (c-1) >= 0 and not checked[r][c-1]
            up = (r-1) >= 0 and c >= 0 and not checked[r-1][c]

            # go right
            if right:
                if not(up and go_dir == [-1, 0]):
                    go_dir = [0, 1]
            # go down
            elif down:
                go_dir = [1, 0]
            # go left
            elif left:
                go_dir = [0, -1]
            # go up
            elif up:
                go_dir = [-1, 0]
            else:
                break

            r = go_dir[0] + r
            c = go_dir[1] + c
            
        return result
