from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curSub = sum(nums[:k])
        maxAvg = curSub / k
        for i in range(len(nums) - k):
            curSub -= nums[i]
            curSub += nums[i + k]
            maxAvg = max(maxAvg, curSub / k)
        return maxAvg

# initialise the current sub
# find the output based on that
# apply sliding window with i and i + k
# recalculate output based on that
# return output