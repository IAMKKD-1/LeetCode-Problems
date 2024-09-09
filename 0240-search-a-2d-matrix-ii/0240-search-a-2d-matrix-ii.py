class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            current = matrix[row][col]
            if target == current:
                return True
            elif target < current:
                col -= 1
            else:
                row += 1

        return False