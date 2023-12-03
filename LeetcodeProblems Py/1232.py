# beats 70% in time and 66% in space

class Solution:
  def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

    (x0, y0), (x1, y1) = coordinates[:2]
    for x, y in coordinates:
      if (y - y1)*(x1 - x0) != (y1 - y0)*(x - x1):
        return False
    return True 