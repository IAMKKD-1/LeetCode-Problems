class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        y = 0
        x = len(matrix)-1
        while y <= x:
            matrix[y], matrix[x] = matrix[x], matrix[y]
            x -= 1
            y+= 1
        
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
