class Solution:
  def countEven(self, num: int) -> int:
    return len([1 for n in range(2, num + 1) if not sum(int(x) for x in str(n)) % 2])

# count the number of integers with an even digit sum
