from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur = sum(arr[:k]) / k
        l, res = 0, 0
        for r in range(k, len(arr)):
          if cur >= threshold:
            res += 1
          cur = (cur * k + arr[r] - arr[l]) / k
          l += 1
        return res + int(cur >= threshold)

# first, we calculate the average of the first k elements
# then we move the window to the right, updating the average
# if the average is greater than or equal to the threshold, we increment the result
# finally, we add 1 to the result if the average of the last k elements is greater than or equal to the threshold
# this is because the last k elements are not included in the loop
# therefore, we need to check if the average of the last k elements is greater than or equal to the threshold
