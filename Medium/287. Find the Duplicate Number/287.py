from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# notice that the length is n + 1, and nums[i] is constrainted to <= n
# so, we can use the indexing of the value in nums as a .next
# hence, this is the same as detecting a linked list cycle
# there is a cycle as two values point to the same value