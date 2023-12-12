from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        H, mx = len(heights), heights[0]
        stk = []
        for idx, height in enumerate(heights):
            lst = idx
            while stk and height < stk[-1][1]:
                i, h = stk.pop()
                mx = max(mx, h * (idx - i))
                lst = i
            stk.append((lst, height))
        for idx, height in stk:
            mx = max(mx, height * (H - idx))
        return mx

# we store the length of heights in stack
# we set max area to be the first height
# we initialise an empty stack

# we iterate through the heights
# we set last to be the current index
# this tracks the last index of the height greater than or equal to the current height

# we pop the stack while the current height is less than the height in the stack
# we set i and h to be the index and height of the popped element
# set max area to be the max of the current max area and the area of the popped element to the current index

# we append the last index and current height to the stack
# this is because we have a rectangle of height h from the last index where the height is greater than or equal to h

# we iterate through the stack after the loop
# we set i and h to be the index and height of the popped element
# set max area to be the max of the current max area and the area of the popped element to the end of the heights

# we return the max area