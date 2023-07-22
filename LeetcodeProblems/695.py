# beats 50% in time and 9% in space

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        ans = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1

        def dfs(row, col):
            if (row, col) in seen:
                return 
            seen.add((row, col))
            for x, y in directions:
                if isValid(row + x, col + y):
                    dfs(row + x, col + y)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in seen and isValid(row, col):
                    start = len(seen)
                    dfs(row, col)
                    end = len(seen)
                    ans = max(ans, end - start)
        return ans