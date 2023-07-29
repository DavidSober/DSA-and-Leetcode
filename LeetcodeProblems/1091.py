# first ever bfs graph problem. I figured out how to do this without a prior 
# template or lesson. It is very similar in logic to bin tree bfs and uses needed
# elements for grid traversal such as valid moves and directions to attempt
# beats 47% in time and 21% in space

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        seen = set([0,0])
        queue = deque([[0,0]])
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        ans = 0
        def isValid(row, col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 0 and (row, col) not in seen
        found = False
        while queue:
            ans += 1
            #print([[x,y] for x, y in queue])
            if [len(grid) - 1, len(grid[0]) - 1] in queue:
                found = True
                break
            
            for _ in range(len(queue)):

                curr = queue.popleft()

                for x, y in directions:
                    if isValid(curr[0] + x, curr[1] + y):
                        queue.append([curr[0] + x, curr[1] + y])
                        seen.add((curr[0] + x, curr[1] + y))
            
        if not found:
            return -1
        return ans 