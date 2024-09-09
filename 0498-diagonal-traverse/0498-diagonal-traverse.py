class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans = []
        if not mat: return ans
        d = {}
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if i+j not in d:
                    d[i+j] = [mat[i][j]]
                else:
                    d[i+j].append(mat[i][j])
        for i in d.items():
            if i[0] % 2 == 0:
                [ans.append(j) for j in i[1][::-1]]
            else:
                [ans.append(j) for j in i[1]]
        return ans