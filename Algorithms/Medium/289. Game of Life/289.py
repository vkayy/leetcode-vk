from typing import List

class Solution:
  def gameOfLife(self, board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    m, n = len(board), len(board[0])
    nxt = [[0] * n for _ in range(m)]
    nbs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(m):
      for j in range(n):
        cnt = sum(board[i + di][j + dj] for di, dj in nbs if 0 <= i + di < m and 0 <= j + dj < n)
        if board[i][j] and 2 <= cnt <= 3:
          nxt[i][j] = 1
        elif not board[i][j] and cnt == 3:
          nxt[i][j] = 1
    for i in range(m):
      for j in range(n):
        board[i][j] = nxt[i][j]

# the idea is to use a 2D array to store the next state of the board
# we use a nested for loop to iterate through the board
# we use a nested for loop to iterate through the neighbours of each cell 
# we use a list comprehension to calculate the number of live neighbours
# we use a nested for loop to iterate through the board
# we update the board with the next state
