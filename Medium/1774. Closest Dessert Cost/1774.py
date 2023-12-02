from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        mxc = max(baseCosts) + sum(toppingCosts) * 2
        dp = [False] * (mxc + 1)
        
        for bc in baseCosts:
            dp[bc] = True
        
        for tc in toppingCosts:
            for c in range(mxc, tc - 1, -1):
                if dp[c - tc]:
                    dp[c] = True
                    continue
                elif c - tc * 2 >= 0 and dp[c - tc * 2]:
                    dp[c] = True
                    continue
        
        return min([i for i, valid in enumerate(dp) if valid], key=lambda x: abs(target - x))
    
# we set mxc to the maximum base cost plus the sum of the topping costs times 2
# this evaluates to the maximum cost possible
# we create a list called dp that is the size of mxc + 1
# this stores whether a cost is possible

# we iterate through the base costs
# for each base cost, we set the index of the base cost in dp to True

# then, we iterate through the topping costs
# for each topping cost, we iterate through the range of mxc to tc - 1, backwards
# by iterating backwards, we can avoid double counting

# if the cost minus the topping cost is possible, we set the cost to True
# if the cost minus the topping cost times 2 is possible, we set the cost to True
# the cost with no topping is always possible due to the base costs

# finally, we return the closest cost to the target