# beats 69% in time and 92% in space

class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:

        d1 = [grid[i][i] for i in range(len(grid))]
        d2 = [grid[i][len(grid)-i-1] for i in range(len(grid))]

        for i in range(len(grid)): # there should only be two diag elements per row no matter what
            count = 0
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    count += 1
                if count > 2: # if we find more than 2 non zero nums it is false
                    return False

        for i in d1:
            if i == 0:
                return False
        for i in d2:
            if i == 0:
                return False
        # now we know the diagnals are fine
        return True 