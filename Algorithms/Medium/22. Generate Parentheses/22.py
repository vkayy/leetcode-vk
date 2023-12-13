from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(o, c, cur):
            nonlocal res
            if o == n and c == n:
                res.append(cur)
            if o > c:
                backtrack(o, c + 1, cur + ")")
            if o < n:
                backtrack(o + 1, c, cur + "(") 
        backtrack(0, 0, "")
        return res

# initialise the result
# define a backtrack function that takes in the number of open and close parentheses and the current string

# if the number of open and close parentheses is equal to n
# then, we can append the current string to the result

# if we have more open parentheses than close parentheses
# then, we can add a close parenthesis to the current string

# also, if we have less open parentheses than n
# then, we can add an open parenthesis to the current string