# this is one of my older solutions from when i was new to DSA
# brute force breats 16% in time and 99% in space

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        rows = grid
        col = [] 

        # gets columns from grid 
        def getcols(arr):    
            for i in range(len(arr)):
                col.append([])
                for row in grid:
                    col[i].append(row[i])
            
        getcols(grid[0])

        # compare rows to cols then return number of matches
        count = 0
        for row in grid:
            for column in col:
                if row == column:
                    count += 1


        return count