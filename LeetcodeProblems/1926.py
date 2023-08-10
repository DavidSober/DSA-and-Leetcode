# beats 65% in time and 28% in space

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def isValid(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != '+' and (row, col) not in seen
        def isExit(row, col):
            return maze[row][col] == '.' and [row, col] != entrance and (row == len(maze) - 1 or row == 0 or col == 0 or col == len(maze[0]) - 1)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([entrance])
        seen = set(entrance)
        ans = 0
        found = False
        while queue:
            if found:
                break
            ans += 1
            for _ in range(len(queue)):
                curr = queue.popleft()

                for x, y in directions:
                    if isValid(curr[0] + x, curr[1] + y):
                        if isExit(curr[0] + x, curr[1] + y):
                            found = True
                        queue.append([curr[0] + x, curr[1] + y])
                        seen.add((curr[0] + x, curr[1] + y))
        if not found:
            return -1
        return ans