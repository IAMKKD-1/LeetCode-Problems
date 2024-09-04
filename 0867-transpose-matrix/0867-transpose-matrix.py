class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new = [[0]*len(matrix) for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                new[j][i] = matrix[i][j]
                # matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return new
