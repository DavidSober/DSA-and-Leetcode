# beats 78% in time and 94% in space

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        R = len(matrix)
        C = len(matrix[0])
        rows = set()  # we store the indexes of 0s into the rows and cols sets respectivly 
        cols = set()

        for i in range(R):          # first we go through the matrix and if we find a zero we add its row and col index to the hash sets
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(R):          # now we go through again and check every element, if it has an index that had a zero we set it to zero
            for j in range(C):
                if i in rows or j in cols:
                    matrix[i][j] = 0