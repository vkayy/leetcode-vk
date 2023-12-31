class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        mx, fst = -1, {}
        for i, ch in enumerate(s):
          if ch not in fst:
            fst[ch] = i
          else:
            mx = max(mx, i - fst[ch] - 1)
        return mx

# if the character has not been seen before
# we add it to fst with its index (earliest occurrence)
# otherwise, update the max length of the substring between equal characters
# return mx