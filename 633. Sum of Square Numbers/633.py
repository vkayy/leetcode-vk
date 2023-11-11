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
