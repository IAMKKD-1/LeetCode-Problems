class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix)
        j = len(matrix[0]) 
        row = 0
        col = j - 1

        while row < i and col > -1:
            cur = matrix[row][col]
            if cur == target: 
                return True
            if target > cur: 
                row += 1
            else:
                col -= 1
        return False

