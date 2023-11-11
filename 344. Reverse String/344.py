from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        N = len(s)
        i, j = 0, N - 1
        while i < j and N > 1:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1

# here we use two pointers
# if the length of s is 1, it is symmetric
# otherwise, set i to be the first index and N to be the last index
# use a temporary var to swap the values
# increment i and decrement j