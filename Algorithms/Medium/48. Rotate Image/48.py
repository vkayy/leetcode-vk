from typing import List

class Solution:
  def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    for i in range(n):
      for j in range(i, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
      l, r = 0, n - 1
      while l < r:
        matrix[i][l], matrix[i][r] = matrix[i][r], matrix[i][l]
        l, r = l + 1, r - 1

# first, we find the transpose of the matrix
# then, for each row
# we reverse the row
# finally, we return the result
# this gives a 90 degree clockwise rotation of the matrix
