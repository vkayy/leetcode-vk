from typing import List

class Solution:
  def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
    points.sort()
    return max(x - points[i - 1][0] for i, (x, y) in list(enumerate(points))[1:])
  
# first, sort the points by x-coordinate
# then, find the maximum difference between two consecutive x-coordinates