from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        
        npks = [-1] * len(height)
        mxi = len(height) - 1
        for i in range(len(height) - 2, -1, -1):
            if height[i] > height[mxi]:
                mxi = i
            npks[i] = mxi
        
        lst, res = 0, 0
        for cur in range(1, len(height)):
            if height[cur] < height[lst]:
                npk = npks[cur]
                if (mxm := min(height[lst], height[npk])) > height[cur]:
                    res += mxm - height[cur]
            else:
                lst = cur
        return res

# here we use dynamic programming to solve the problem

# we create a list called npks that stores the index of the next peak
# note that the next peak is the peak with the greatest height after the current index
# the last next peak is -1 because there is no next peak

# we set mxi to the index of the last peak
# we iterate through the height backwards
# if the height at the current index is greater than the height at the last peak
# we set the last peak index to the current index
# we set the next peak at the current index to the last peak index

# we set lst to the index of the last peak
# we set res to 0

# we iterate through the height starting from the second index
# this is because we need to compare the current index with the previous index

# if the height at the current index is less than the height at the last peak
# we set npk to the next peak at the current index

# set mxm to the minimum of the height of the surrounding peaks
# if the minimum is greater than the height at the current index
# we add the difference to res

# if the height at the current index is greater than the height at the last peak
# we set the last peak index to the current index

# finally, we return res