from functools import lru_cache

class Solution:
  @lru_cache()
  def minDays(self, n: int) -> int:
    return 1 + min(n % 2 + self.minDays(n // 2), n % 3 + self.minDays(n // 3)) if n > 1 else n

# we cache the results of the recursive calls to avoid redundant calculations
# if the number is greater than 1, return 1 plus the minimum of of our choices, accounting for indivisibility
# we use the module to account for the case where the number is not divisible by 2 or 3, as we would just eat one orange at a time
# if the number is 1, return 1
# if the number is 0, return 0
