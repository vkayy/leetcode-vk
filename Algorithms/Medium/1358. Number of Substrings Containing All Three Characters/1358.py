class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res, lst = 0, [-1, -1, -1]
        for i, ch in enumerate(s):
            lst[ord(ch) - 97] = i
            res += 1 + min(lst)
        return res     
      
# at each point, we update the index of the last occurrence of the character
# then we add 1 + the minimum index to the result
# this is because for each valid substring starting at i, each substring ending at j (i <= j) is valid
# therefore, we add 1 + min(lst) to the result
