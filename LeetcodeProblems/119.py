# my first recurion + memoization problem
# beats 80% in time and 5% in space

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        numcols = rowIndex
        cache = {}
        def Pnum(row, col):
            if row == 0 or col == 0 or row == col:
                return 1
            if (row, col) in cache:
                return cache[(row, col)]
            else:
                result = Pnum(row - 1, col - 1) + Pnum(row - 1, col) 
            cache[(row, col)] = result
            return result
        ans = []
        for i in range(rowIndex + 1):
            ans.append(Pnum(rowIndex, i))
        return ans