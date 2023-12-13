from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dpa = [float("inf")] * (amount + 1)
        dpa[0] = 0
            
        for j in range(1, amount + 1):
            
            for i in range(0, len(coins)):
                
                if coins[i] <= j:
                    if (new := 1 + dpa[j - coins[i]]) < dpa[j]:
                        dpa[j] = new
            
        return dpa[amount] if dpa[amount] != float("inf") else -1

# first, we create a list of size amount + 1 filled with infinity
# this is so that the first minimum we find will be the minimum
# we set the first element to 0 as we need 0 coins to make 0 cents

# then, we iterate through the amounts
# this is because we are trying to find the minimum number of coins to make the amount

# then, we iterate through the coins
# this is because we are trying to find the minimum number of coins to make the amount using the current coin

# if the coin is less than or equal to the amount, it can be used to make the amount

# if the minimum coins to make the amount using the current coin is less than the current minimum coins to make the amount
# we set the current minimum coins to make the amount to the minimum coins to make the amount using the current coin plus 1

# finally, we return the minimum coins to make the amount if it is not infinity