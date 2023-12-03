# beats 61% in time and 14% in space

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        numneg = 0
        for row in grid:
            for num in row:
                if num < 0:
                    numneg += 1
        return numneg