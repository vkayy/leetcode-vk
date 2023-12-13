
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = {
            "+": lambda x,y: x + y,
            "-": lambda x,y: x - y,
            "*": lambda x,y: x * y,
            "/": lambda x,y: int(x / y)
        }
        for t in tokens:
            if t in ops:
                o1, o2 = stk.pop(), stk.pop()
                stk.append(ops[t](o2, o1))
            else:
                stk.append(int(t))
        return stk[0]

# initialise a stack
# initialise a dictionary of operations

# for each token in the tokens
# if the token is an operation
# then, pop the last two elements from the stack
# then, push the result of the operation to the stack

# otherwise, push the token to the stack
# return the first element of the stack
# this is because the stack will only have one element left