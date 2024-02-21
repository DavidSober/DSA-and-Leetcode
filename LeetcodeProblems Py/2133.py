class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        cols = list(zip(*matrix))

        for i in range(len(matrix)):
            col = cols[i]
            row = [matrix[i][j] for j in range(len(matrix[i]))]
            row = sorted(row)
            col = sorted(col)
            for j in range(len(row) - 1):
                if row[j + 1] - row[j] != 1 or col[j + 1] - col[j] != 1:
                    return False
        return True