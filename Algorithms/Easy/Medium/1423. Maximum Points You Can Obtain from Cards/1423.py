from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        curSum = sum(cardPoints[-k:])
        maxSum = curSum
        for i in range(-k, 0):
            curSum -= cardPoints[i]
            curSum += cardPoints[i + k]
            maxSum = max(maxSum, curSum)
        return maxSum

# first, set curSum to the last three summed
# set maxSum to initial curSum
# now, from -k to -1,
# shift curSum across from the right side to the left
# find the maximum
# return the max