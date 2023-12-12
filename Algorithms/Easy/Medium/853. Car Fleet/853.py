from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed))
        stk = []
        for p, s in cars:
            while stk and s < stk[-1][1]:
                if p + s * (p - stk[-1][0]) / (stk[-1][1] - s) <= target:
                    stk.pop()
                else:
                    break
            stk.append((p, s))
        return len(stk)

# initialise a list of tuples of the position and speed of the cars
# sort in non-decreasing order of position
# initialise a stack

# iterate through the list of tuples

# while the stack is non-empty and the speed of the current car is less than the speed of the car at the top of the stack
# check to see if the current car will catch up to the car at the top of the stack by the time it reaches the target
# if so, then we can pop the car at the top of the stack
# otherwise, we can break out of the loop

# then, we can push the current car to the stack

# return the length of the stack