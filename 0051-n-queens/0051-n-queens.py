class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sol = []
        chess = [['.']*n for _ in range(n)]
        visited_col = set()
        visited_row = set()
        visited_diag_sum = set()
        visited_diag_diff = set()

        def backtrack(row):
            if row == n:
                sol.append([''.join(i) for i in chess])
                return 

            for c in range(n):
                diag_sum = row+c
                diag_diff = c-row

                if (row in visited_row or c in visited_col or diag_sum in visited_diag_sum or diag_diff in visited_diag_diff):
                    continue

                visited_row.add(row)
                visited_col.add(c)
                visited_diag_sum.add(diag_sum)
                visited_diag_diff.add(diag_diff)
                chess[row][c] = 'Q'
                backtrack(row+1)
                chess[row][c] = '.'
                visited_row.remove(row)
                visited_col.remove(c)
                visited_diag_sum.remove(diag_sum)
                visited_diag_diff.remove(diag_diff)

        backtrack(0)
        return sol