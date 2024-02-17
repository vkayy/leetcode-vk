from typing import List
import heapq

class Solution:
  def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    gaps, h = [], len(heights)
    for i in range(h - 1):
      if (gap := heights[i + 1] - heights[i]) > 0:
        heapq.heappush(gaps, gap)
      if len(gaps) > ladders:
        bricks -= heapq.heappop(gaps)
      if bricks < 0:
        return i
    return h - 1

# the idea is to use a greedy algorithm to use ladders for the largest gaps
# we use a min heap to store the gaps

# we iterate through the heights
# if the gap is positive, we add it to the min heap, as we cannot climb down
# if the min heap is larger than the number of ladders, we use bricks to climb the smallest gap
# if we run out of bricks, we return the current index
# if we reach the end, we return the last index
