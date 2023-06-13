# this is the most optimal solution it involves flattening the matrix
# without using any extra space. you can access the mid's row and cols by
# // n and % n which is crazy useful to know for future ref
# beats 72% in time and 51% in space

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // n
            col = mid % n
            if matrix[row][col] == target:
                return True
            if matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False



# my first solution to this problem was close to the most optimal sol but not quite there
# beats 6% in time and 51% in space

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # find which row
        if len(matrix[0]) < 4:
            for row in matrix:
                for num in row:
                    if num == target:
                        return True
            return False

        row = None
        for i in range(len(matrix) - 1):
            if matrix[i][0] <= target < matrix[i + 1][0]:
                row = i
        if row == None: # potentially the last row
            row = len(matrix) - 1
        pot = bisect.bisect_left(matrix[row], target)
        if pot >= len(matrix[0]):
            return False
        print(row, pot)
        if matrix[row][pot] == target:
            return True
        else:
            False