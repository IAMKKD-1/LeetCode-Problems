class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        total = 0
        n = len(mat)
        for i in range(n):
            total += mat[i][i]
            total += mat[i][n - i - 1]
        if n%2 == 1:
            total -= mat[n//2][n//2]
        return total