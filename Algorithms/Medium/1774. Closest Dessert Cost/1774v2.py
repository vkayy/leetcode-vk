from functools import cache
from typing import List

class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        
        @cache
        def dp(i, cost):
            if i == len(toppingCosts) or cost > target:
                return cost
            tc = toppingCosts[i]
            i += 1
            cs = [dp(i , cost), dp(i , cost + tc), dp(i , cost + tc * 2)]
            return min(cs, key=lambda x: (abs(target - x), x))
        
        bcs = [dp(0, bc) for bc in baseCosts]
        return min(bcs, key=lambda x: (abs(target - x), x))
    
# we define a function called dp that takes in an index and a cost

# if we have reached the end of the topping costs or cost exceeds target, return cost
# this is because we have evaluated the final cost in the topping costs
# or, the cost is beyond the target, so evaluating further will decrease closeness

# we set tc to the topping cost at the index
# we increment the index
# we set cs to the result of dp with the index and cost

# cs contains the closest cost to target out of three paths:
# adding no topping, adding one topping, and adding two toppings
# we then return the closest cost out of cs

# we set bcs to the result of dp with 0 and each base cost
# bcs contains the closest cost to target out of all base costs

# finally, we return the closest cost out of bcs to target