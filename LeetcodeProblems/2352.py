# here is my revised approach. it uses a fast and simple method to get access to cols
# beats 61% in time and 82% in space

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        RF = Counter()
        rows = [tuple(row) for row in grid]
        for row in rows:
          RF[row] += 1
        pairs = 0
        for col in zip(*grid):
            pairs += RF[col]
        return pairs

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