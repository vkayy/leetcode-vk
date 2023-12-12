from itertools import groupby

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return ''.join(str(len(list(group))) + digit for digit, group in groupby(self.countAndSay(n - 1)))

# we can use recursion to generate the nth term
# if n is 1, we can return "1"

# otherwise, we can return the result of countAndSay(n - 1)
# we can use groupby to group consecutive digits
# we can use list to convert the groupby object to a list
# we can use len to get the length of the list
# we can use str to convert the length to a string
# we can use digit to get the digit
# we can use str to convert the digit to a string
# we can use + to concatenate the length and digit
# we can use join to join the list of strings