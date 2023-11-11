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
            k, k = i + 1, N - 1
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

# set the vars for list size and best sum
# sort the list
# if the size is 3, the bestsum will just be the first three elements summed
# iterating through 0 to n-2
# if i is greater than 0 and it has the same value as the previous i, skip
# set j to i + 1, and k to the final index
# while j is less than k
# set the current sum to the sum of values
# if the current sum is the target, return it, as we have reached the target
# if not, check to see whether the current sum is closer to the target than the best sum
# if it is, set the bestsum to the current sum
# if the current sum is less than the target, increment j
# while j is less than k and the value at j is the same as that at j - 1, increment j
# if the current sum is greater than the target, decrement k
# while j is less than k and the value at k is the same as that at k + 1, decrement k
# return the best sum