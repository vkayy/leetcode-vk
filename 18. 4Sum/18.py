from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        N, result = len(nums), []
        nums.sort()
        for i in range(N - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, N - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                k, l = j + 1, N - 1
                newTarget = target - nums[i] - nums[j]
                while k < l:
                    if nums[k] + nums[l] > newTarget:
                        l -= 1
                    elif nums[k] + nums[l] < newTarget:
                        k += 1
                    else:
                        result.append([nums[i], nums[j], nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < l and nums[k] == nums[k - 1]:
                            k += 1
                        while k < l and nums[l] == nums[l + 1]:
                            l -= 1
        return result

# observe the innermost for loop
# similarly to 3sum, the low and high are set to:
# j + 1 and the array size - 1
# iterate through indices i of nums up to N-3
# if the value at the current index is the same as the previous
# skip, as this will give non-unique solutions ()
# iterate through indices j of nums from i + 1 up to N-2
# if the value at the current index is the same as the previous
# skip, as this will give non-unique solutions ()
# set k to be one more than j, and l to be N - 1
# set the new target to be the original target subtract nums[i] and nums[j]
# while k is less than l
# if the value at k and l sum to more than the new target, decrement l
# if the value at k and l sum to less than the new target, increment k
# otherwise, the value at k and l sum to the new target
# append this solution to the result
# increment k, but if nums[k] is equal to nums[k - 1], increment k again
# decrement l, but if nums[l] is equal to nums[l + 1], decrement l again
# we skip the identical soltuiosn
# return the result