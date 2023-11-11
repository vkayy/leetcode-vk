from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        N, bestSum = len(nums), nums[0] + nums[1] + nums[2]
        nums.sort()
        if N == 3:
            return bestSum
        for i in range(N - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, N - 1
            while j < k:
                curSum = nums[i] + nums[j] + nums[k]
                if curSum == target:
                    return target
                if abs(target - curSum) < abs(target - bestSum):
                    bestSum = curSum
                if curSum < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return bestSum   