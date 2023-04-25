# beats 44% in time and 18% in space

class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        minrow = []
        for row in matrix:
            minrow.append(min(row))
        mincol = []
        cols = []
        for j in range(len(matrix[0])):
            newcol = []
            for i in range(len(matrix)):
                newcol.append(matrix[i][j])
            cols.append(newcol)
        
        for i in cols:
            mincol.append(max(i))
        
        ans = []
        for x in minrow:
            if x in mincol:
                ans.append(x)
        return ans