from typing import List

class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    res = [[1]]
    for i in range(numRows - 1):
      pad = [0] + res[-1] + [0]
      cur = []
      for j in range(1, len(pad)):
        cur.append(pad[j] + pad[j - 1])
      res.append(cur)
    return res

# first, initialize the first row
# then, for each row
# pad the previous row with 0s
# then, for each element in the padded row
# add the element and the previous element
# return the result
