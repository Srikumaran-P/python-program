class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None. Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return  # ⚠️ Empty battlefield — no souls to save

        row, col = len(board), len(board[0])

        # 🗡️ Kenpachi-style dive into Hollow-infested zones
        def dfs(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or board[i][j] != 'O':
                return
            board[i][j] = 'T'  # 🛡️ Kido shield: Temporarily mark this soul as protected
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)

        # 🔰 Phase 1: Shield the border souls
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O' and (i in [0, row - 1] or j in [0, col - 1]):
                    dfs(i, j)  # Send in the captains to secure the edge

        # ☠️ Phase 2: Cleanse the corrupted (trapped souls)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'  # 🩸 Soul lost to Hollowfication

        # 🌟 Phase 3: Restore the protected souls
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'T':
                    board[i][j] = 'O'  # ✨ Soul safely returned to Soul Society
