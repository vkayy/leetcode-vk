class Solution:
    def reverse(self, x: int) -> int:
        rev, mn, mx = 0, -2 ** 31, 2 ** 31 - 1
        while x != 0:
            if rev < mn / 10 or rev > mx / 10:
                return 0
            digit = x % 10 if x > 0 else x % -10
            x = int(x / 10)
            rev = rev * 10 + digit
        return rev

# first, initialise rev, mn, mx to 0, -2 ** 31, 2 ** 31 - 1 respectively
# this is because the range of 32-bit signed integers is [-2 ** 31, 2 ** 31 - 1]

# while x is not 0
# if rev is less than mn / 10 or rev is greater than mx / 10, return 0
# this is because if rev is less than mn / 10 or rev is greater than mx / 10, rev * 10 + digit will overflow

# digit is x % 10 if x is greater than 0, else digit is x % -10
# this is because if x is negative, x % 10 will not return a negative number
# for example, -123 % 10 = 7, but we want it to be -3

# x is x / 10
# rev is rev * 10 + digit

# return rev