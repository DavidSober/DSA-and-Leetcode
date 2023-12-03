# beats 98% in time and 47% in space

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        d1 = [mat[i][i] for i in range(len(mat))]
        d2 = [mat[i][len(mat) - i - 1] for i in range(len(mat))]
        if len(mat) % 2 == 1:
            return sum(d1) + sum(d2) - mat[len(mat)//2][len(mat)//2]
        else:
            return sum(d1) + sum(d2) 