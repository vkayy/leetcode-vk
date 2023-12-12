import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, math.floor(math.sqrt(c))
        while a <= b:
            if a ** 2 + b ** 2 > c:
                b -= 1
            elif a ** 2 + b ** 2 < c:
                a += 1
            else:
                return True
        return False

# the maximum value of b is the rounded square root of c
# while a is less than or equal to b
# if the square sum is greater than c
# decrement b
# if the square sum is less than c
# increment a
# if equal, return True
# otherwise, return false