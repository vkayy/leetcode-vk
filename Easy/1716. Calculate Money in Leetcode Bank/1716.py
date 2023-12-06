class Solution:
    def totalMoney(self, n: int) -> int:
        return sum(i % 7 + i // 7 if i % 7 != 0 else i // 7 + 6 for i in range(1, n + 1))

# this works by iterating through the range of 1 to n + 1
# if the number is not divisible by 7, we add the remainder to the quotient
# if the number is divisible by 7, we add 6 to the quotient
# this is because the first week is 1 + 2 + 3 + 4 + 5 + 6 + 7
# the second week is 2 + 3 + 4 + 5 + 6 + 7 + 8
# and so on