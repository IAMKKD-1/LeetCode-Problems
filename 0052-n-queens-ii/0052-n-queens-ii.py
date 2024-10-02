class Solution:
    def totalNQueens(self, n: int) -> int:
        sol = [0]
        board = [['.']*n for _ in range(n)]
        cols = set()
        diag_add = set()
        diag_diff = set()

        def backtrack(row):
            if row == n:
                sol[0] += 1
                return

            for col in range(n):
                add = row+col
                diff = col-row

                if col in cols or add in diag_add or diff in diag_diff:
                    continue
                
                cols.add(col)
                diag_add.add(add)
                diag_diff.add(diff)
                board[row][col] = 'Q'

                backtrack(row+1)

                cols.remove(col)
                diag_add.remove(add)
                diag_diff.remove(diff)
                board[row][col] = '.'

        backtrack(0)
        return sol[0]