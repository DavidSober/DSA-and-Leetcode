# beats 46% in time and 98% in space!

class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        entire = []
        for row in grid:
            for n in row:
                entire.append(n)
        entire.sort()
        return entire[len(entire)//2]