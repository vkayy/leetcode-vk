from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            
            for word in wordDict:
                
                if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
                    
                if dp[i]:
                    break
        
        return dp[0]

# first, we create a list of size len(s) + 1 filled with False
# this means that we cannot make any substrings by breaking at any index
# we set the last element to True as we can make an empty string by breaking at the last index

# then, we iterate through the string backwards
# this is because our recurrence relation depends on the substring starting at i + len(word)
# hence, our base case is the substring starting at the last index

# then, we iterate through the words in the word dictionary

# if the current break at i + len(word) is in bounds and the substring matches the current word
# we set dp[i] to true, as we can break at i to make the substring

# if dp[i] is true, we break, as we only need to find one way to break at i

# finally, we return dp[0] as this returns whether we can break the entire string
