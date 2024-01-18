from typing import List

class Solution:
  def minOperations(self, nums: List[int]) -> int:
    return sum(n.bit_count() for n in nums) + len(bin(max(nums))) - 3

# first, we count the number of 1s in each number
# this is the number of operations we need to perform to make the number 0
# then, we find the maximum number in the array
# we convert it to binary and count the number of digits
# we subtract 3 as the first 2 digits are '0b'
# and, we only need to divide by 2 (l - 1) times to get to 0
