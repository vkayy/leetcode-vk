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