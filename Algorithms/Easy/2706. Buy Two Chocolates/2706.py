from typing import List

class Solution:
  def buyChoco(self, prices: List[int], money: int) -> int:
    mn1 = mn2 = float("inf")
    for price in prices:
      if price < mn1:
        mn2 = mn1
        mn1 = price
      elif price < mn2:
        mn2 = price
    return money if mn1 + mn2 > money else money - mn1 - mn2

# set mn1 and mn2 to infinity
# loop through the prices
# if the price is less than mn1, then set mn2 to mn1 and mn1 to the price
# otherwise, if the price is less than mn2, then set mn2 to the price
# if mn1 + mn2 is greater than money, then return money
# otherwise, return money - mn1 - mn2, i.e., money left after buying