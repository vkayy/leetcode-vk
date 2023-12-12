class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for d in range(9, -1, -1):
            if (tr := str(d) * 3) in num:
                return tr
        return ""

# starting from 9, iterate through the digits in descending order
# if the concatenation of 3 of the same digit is in num, return it
# otherwise return ""