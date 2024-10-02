class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def backtrack(row, col, t):
            if t == len(word):
                return True

            letter = word[t]

            if row < 0 or col < 0 or row >= m or col >= n or board[row][col] != letter:
                return False

            temp = board[row][col]
            board[row][col] = '#'
            
            up = backtrack(row-1, col, t+1)
            down = backtrack(row+1, col, t+1)
            left = backtrack(row, col-1, t+1)
            right = backtrack(row, col+1, t+1)

            board[row][col] = temp

            return up or down or left or right
        
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and backtrack(i, j, 0):
                    return True
        return False
