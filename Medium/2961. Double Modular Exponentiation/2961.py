from typing import List

class Solution:
    def getGoodIndices(self, variables: List[List[int]], target: int) -> List[int]:
        res = []
        for i, [a, b, c, m] in enumerate(variables):
            if pow(pow(a, b, 10), c, m) == target:
                res.append(i)
        return res

# first, we can create a list to store the indices of the good variables

# then, we can iterate through the variables
# if the variable is good, we can append the index to the list

# then, we can return the list