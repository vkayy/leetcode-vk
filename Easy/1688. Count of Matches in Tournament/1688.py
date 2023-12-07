class Solution:
    def numberOfMatches(self, n: int) -> int:
        rs = 0
        while n > 1:
            if n % 2 == 0:
                rs += n // 2
                n //= 2
            else:
                rs += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return rs

# if n is even, add n // 2 to rs and set n to n // 2
# if n is odd, add (n - 1) // 2 to rs and set n to (n - 1) // 2 + 1
# repeat until n is 1
# return rs