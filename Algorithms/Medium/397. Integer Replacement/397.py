from functools import lru_cache

class Solution:
  @lru_cache(None)
  def integerReplacement(self, n: int) -> int:
    return 0 if n == 1 else (1 + min(1 + self.integerReplacement((n + 1) // 2), self.integerReplacement(n - 1)) if n % 2 else 1 + self.integerReplacement(n // 2))     

# we can either increment the number by 1 or decrement the number by 1 if the number is odd
# if the number is even, we can divide the number by 2
# to ensure we do not branch out subproblems, we immediately divide the number by 2 if we add 1 to the number
