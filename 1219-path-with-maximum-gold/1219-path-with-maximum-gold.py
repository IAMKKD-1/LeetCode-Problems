class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = 0
        m = len(grid)
        n = len(grid[0])

        def backtrack(row, col, gold):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == 0:
                return gold

            curr = grid[row][col]
            grid[row][col] = 0

            up = backtrack(row-1, col, gold + curr)
            down = backtrack(row+1, col, gold + curr)
            left = backtrack(row, col-1, gold + curr)
            right = backtrack(row, col+1, gold + curr)
            
            grid[row][col] = curr

            return max(up, down, left, right)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                max_gold = max(max_gold, backtrack(i, j, 0))
                
        return max_gold