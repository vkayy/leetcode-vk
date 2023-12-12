from typing import List

class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        s, res = f"{s}#", []
        N, l = len(s), 0
        for r in range(1, N):
            if s[r] != s[l] and r - l >= 3:
                    res.append([l, r - 1])
            if s[r] != s[l]:
                l = r
        return res

# set s to be s with a "#" appended to the end
# this is to make sure we don't miss the last group

# set res to be an empty list
# set N to be the length of s

# set the left pointer to be 0
# iterate the right pointer from 1 to N - 1

# if the current char is diff to the char at the left pointer
# and the length of the substring is greater than or equal to 3
# this means we have a large group
# append the left and right pointers to the result

# if the current char is diff to the char at the left pointer
# set the left pointer to be the right pointer
# this is because we have a new group

# return the result