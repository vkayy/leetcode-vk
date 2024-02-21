class Solution:
  def rangeBitwiseAnd(self, left: int, right: int) -> int:
    return right if left >= right else self.rangeBitwiseAnd(left, right & right - 1)

# the idea is to use the fact that the bitwise AND of a range of numbers is the common prefix of the binary representation of the numbers
# if the range is empty, we return 0
# if the range has only one number, we return the number
# if the range has more than one number, we return the bitwise AND of the range
# we use a recursive approach to calculate the bitwise AND of the range
# if the left number is greater than or equal to the right number, we return the right number
# otherwise, we return the bitwise AND of the left number and the bitwise AND of the left number and the right number minus 1
# the time complexity is O(logN) and the space complexity is O(1)
