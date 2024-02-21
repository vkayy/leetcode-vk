from typing import List

class Solution:
  def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
    items.sort()
    res, N = [], len(items)
    for i in range(1, N):
      items[i][1] = max(items[i][1], items[i - 1][1])
    for q in queries:
      l, r = 0, len(items) - 1
      while l <= r:
        m = (l + r) // 2
        p, _ = items[m]
        if p > q:
          r = m - 1
        else:
          l = m + 1
      res.append(0 if r < 0 else items[r][1])
    return res

# the idea is to use a binary search to find the maximum beauty of the items for each query
# we sort the items

# we iterate through the items
# we update the beauty of the items so that each item has the maximum beauty of the items to its left
# this is because any item to the right is more expensive and thus a query of its price would have at least the beauty of the item to its left

# we iterate through the queries
# we use a binary search to find the maximum beauty of the items for each query
# if the price of the item is greater than the query, we update the right pointer
# this is because the price of the item is greater than the query and thus we need to look for a smaller price
# otherwise, we update the left pointer
# this is because the price of the item is less than or equal to the query and thus we need to look for a greater price
# we append based on the right pointer as it is the maximum price less than or equal to the query
# if the right pointer is less than 0, we append 0 as there is no item with a price less than or equal to the query

# we return the result
