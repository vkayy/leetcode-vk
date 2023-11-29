from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            
        return rob2

# first, we define two variables to store the maximum amount of money we can rob
# rob1 is the maximum amount of money we can rob if we rob the previous house
# rob2 is the maximum amount of money we can rob if we do not rob the previous house

# then, we iterate through the houses

# we set temp to the maximum amount of money we can rob if we rob the current house
# this is the maximum of the current house plus rob1 and rob2
# this is because we cannot rob adjacent houses

# we set rob1 to rob2
# we set rob2 to temp
# this is because we are moving on to the next house

# finally, we return rob2