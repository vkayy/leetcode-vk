from math import log

class Solution:
  def isPowerOfTwo(self, n: int) -> bool:
    return False if n <= 0 else 2 ** int(log(n, 2)) == n

# first, we check if n is less than or equal to 0
# if so, we return False
# otherwise, we return whether 2 raised to the power of the integer part of the base 2 logarithm of n is equal to n
# this is because 2 raised to the power of the integer part of the base 2 logarithm of n is the nearest power of 2 to n
