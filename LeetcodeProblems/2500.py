# beats 88% in time and 48% in space

class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:

        ans = 0

        for i in range(len(grid)): # in place sorting grid rows
            grid[i] = sorted(grid[i], reverse=True)
        #print(grid)
        for i in range(len(grid[0])):
            col = [row[i] for row in grid]
            ans += max(col)
        return ans