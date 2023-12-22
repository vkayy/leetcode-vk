class Solution:
    def maxScore(self, s: str) -> int:
      cur = s.count('1')
      mx = 0
      for i in range(1, len(s)):
        if s[i - 1] == '0':
          cur += 1
        else:
          cur -= 1
        mx = max(mx, cur)
      return mx
  
# first, count number of 1s, and use this as a starting point
# then, iterate through string, and if we find a 0, increment cur
# otherwise, decrement cur
# update mx with max(mx, cur)
# return mx