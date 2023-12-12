from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(0, len(min(strs, key=len))):
            if any(strs[0][i] != strs[j][i] for j in range(1, len(strs))):
                return res
            res += strs[0][i]
        return res

# we can iterate through each character in the shortest string
# we can use any to check if the character is not in the same position in every string
# if it is not, we can return the result
# otherwise, we can add the character to the result

# then, we can return the result