from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        N, result = len(nums), []
        nums.sort()
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k, target = i + 1, N - 1, -nums[i]
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return result

# take the list size and initiate result list
# sort nums
# iterate through all indices i of nums
# if the value at the current index is the same as the previous
# skip, as this will give non-unique solutions ()
# set j to be one more than i, and k to be the final index
# while j is less than k
# if the value at j and k sum to more than the target, decrement k
# if the value at j and k sum to less than the target, increment j
# otherwise, the value at j and k sum to the target
# append this solution to the result
# increment j, but if nums[j] is equal to nums[j - 1], increment j
# we skip the identical solutinos