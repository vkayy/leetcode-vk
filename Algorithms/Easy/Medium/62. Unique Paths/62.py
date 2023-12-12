from math import factorial

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        return factorial(m + n - 2) // factorial(m - 1) // factorial(n - 1)

# first, we import the factorial function from the math module

# then, we define a function that takes in two integers, m and n, and returns an integer
# this function will return the number of unique paths from the top left corner to the bottom right corner of an m x n grid

# to do this, we use the formula for combinations
# the formula for combinations is n! / r! / (n - r)!

# we can think of the grid as a series of moves
# we have to move m - 1 times down and n - 1 times right
# this is because we start at the top left corner and end at the bottom right corner

# essentially, we have m + n - 2 moves to make
# then, we choose m - 1 moves to be down
# this is because we have to make m - 1 moves down to get to the bottom right corner

# finally, we return the result of the formula