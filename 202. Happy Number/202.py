class Solution:
    def isHappy(self, n: int) -> bool:
        def digitSquareSum(n: int) -> int:
            sum = 0
            for i in str(n):
                sum += int(i) ** 2
            return sum
        slow, fast = n, n
        while True:
            slow = digitSquareSum(slow)
            fast = digitSquareSum(digitSquareSum(fast))
            if slow == 1 or fast == 1:
                return True
            if slow == fast:
                return False

# here we create a function to find the square sum of the digits of a number
# use the two pointers
# let digitSquareSum be the next operation
# if either evaluate to 1, return true
# otherwise, return false