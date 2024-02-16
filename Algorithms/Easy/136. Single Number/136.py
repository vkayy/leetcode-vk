from typing import List
from functools import reduce
import operator

class Solution:
  def singleNumber(self, nums: List[int]) -> int:
    return reduce(operator.xor, nums, 0)

# first, we use the reduce function to apply the xor operator to all the numbers in the array
# this is because the xor operator is commutative and associative
# therefore, we can apply the xor operator to all the numbers in the array
# and the result will be the number that appears only once
