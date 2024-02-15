from typing import List

class Solution:
  def jump(self, nums: List[int]) -> int:
    dp, n = [float("inf")] * (len(nums) - 1) + [0], len(nums)
    for i in range(n - 2, -1, -1):
      dp[i] = min((1 + dp[i + j] for j in range(nums[i], 0, -1) if i + j < n), default=float("inf"))
    return dp[0]
