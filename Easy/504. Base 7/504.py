class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"
        res, num, neg = "", abs(num), num < 0
        while num != 0:
            res = str(num % 7) + res
            num //= 7
        return f"-{res}" if neg else res

# if the number is 0, return "0"
# initialize an empty string for the result
# initialize a boolean for whether the number is negative

# while the number is not 0
# add the remainder of the number divided by 7 to the result
# divide the number by 7
# return the result if the number is positive, otherwise return the result with a negative sign