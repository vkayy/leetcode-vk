from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        for sell in range(len(prices)):
            if prices[sell] < prices[buy]:
                buy = sell
            curr = prices[sell] - prices[buy]
            profit = max(curr, profit)
        return profit

# max profit is originally zero
# set the left pointer to zero
# iterate through each index as an end point
# if the current price is lower than the current buy price
# change buy price to current price
# set curr profit to sell minus buy
# take profit to be the max of curren tprofit and profit
# return profit