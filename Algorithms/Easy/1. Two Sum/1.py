from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        for i in range(len(nums)):
            required = target - nums[i]
            if required in numDict:
                return [numDict[required], i]
            numDict[nums[i]] = i

# time: O(n)
# space: O(n)

# first, create a dictionary to store the numbers and their indices
# iterate through the list of numbers
# for each number, calculate the required number to sum to target
# if the required number is in the dictionary, return the indices
# else, add the number and its index to the dictionary