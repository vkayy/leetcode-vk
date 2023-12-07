class Solution:
    def largestOddNumber(self, num: str) -> str:
        odds, i = set("13579"), len(num) - 1
        while i >= 0:
            if num[i] in odds:
                return num[:i + 1]
            i -= 1
        return ""

# an odd number is a number that is not divisible by 2
# we can use a set to store the odd numbers
# we can iterate through the string from the end
# if the current character is in the set, then we can return the string up to the current index
# otherwise, we can decrement the index
# if we reach the start of the string, then we can return an empty string