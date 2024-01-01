from typing import List

class Solution:
  def findContentChildren(self, g: List[int], s: List[int]) -> int:
    g.sort()
    s.sort()
    cur = res = 0
    while res < len(g) and cur < len(s):
      if g[res] <= s[cur]:
        res += 1
      cur += 1
    return res

# first, sort both lists
# then, iterate through both lists
# if the current cookie is big enough for the current child
# increment the child index
# otherwise, move on to the next cookie
# increment the cookie index
# once we have satisfied all children or run out of cookies
# return the number of satisfied children