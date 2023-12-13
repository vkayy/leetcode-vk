from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = [0]
        for i in range(1, len(temperatures)):
            while stk and temperatures[i] > temperatures[stk[-1]]:
                res[stk[-1]] = i - stk[-1]
                stk.pop()
            stk.append(i)
        return res

# initialise the result and a stack

# iterate through the range of 1 to the length of the temperatures

# while the stack is non-empty and the current temp is greater than the element at the top pointer of the stack

# then, we can set the result at the top pointer of the stack to the difference between the current index and the top pointer of the stack
# this is because the current index is the next warmer temperature

# then, we can pop the top pointer of the stack

# then, we can push the current index to the stack

# return the result

# this uses a monotonic stack to store the indices of the temperatures