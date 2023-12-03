from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mxl, mxr = height[l], height[r]
        total = 0
        while l < r:
            mxl, mxr = max(mxl, height[l]), max(mxr, height[r])
            if mxl < mxr:
                total += mxl - height[l]
                l += 1
            else:
                total += mxr - height[r]
                r -= 1
        return total

# we have two pointers, one at the start and one at the end
# we also have two variables to store the max height from the left and right
# we also have a variable to store the total amount of water trapped

# while the left pointer is less than the right pointer

# we update the max height from the left and right

# if the max height from the left is less than the max height from the right
# this means that the max height from the left is the limiting factor
# so we add the difference between the max height from the left and the current height to the total
# and we increment the left pointer

# otherwise, we add the difference between the max height from the right and the current height to the total
# and we decrement the right pointer

# we are shifting based on the minimal max height, which is the limiting factor
# we are guaranteed that the water trapped is the maximum possible

# return the total amount of water trapped