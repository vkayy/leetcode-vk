from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        i, j = 0, len(height) - 1
        while i < j:
            cur = (j - i) * min(height[i], height[j]) 
            if cur > max:
                max = cur
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return max

# initialise the max to 0
# use two pointers
# set the current area to the width multiplied by the min height
# if cur is greater than max, set max to cur
# then, if the height at i is greater than that at j, decrement j
# otherwise, increment i
# thus, return the max