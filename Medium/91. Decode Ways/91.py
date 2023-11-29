class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = { len(s) : 1  }
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            
            if (i + 1 < len(s) and
                (s[i] == "1" or
                 s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] += dp[i + 2]
        
        return dp[0]

# first, we create a dictionary called dp
# this dictionary will store the number of ways to decode the substring starting at i
# we set the value at len(s) to 1
# this is because there is only 1 way to decode an empty string

# then, we iterate through the string backwards
# this is because our recurrence relation depends on the substring starting at i + 1 and i + 2

# if the character at i is "0"
# we set the value at i to 0
# this is because we cannot decode a string that starts with "0"

# otherwise, we set the value at i to the value at i + 1
# this is because we can always decode the substring starting at i by decoding the substring starting at i + 1
# for example, if we have "123", we can decode "123" by decoding "23"

# if i + 1 is in bounds and the character at i is "1" or the character at i is "2" and the character at i + 1 is in "0123456"
# this means that we can decode the substring starting at i by decoding the substring starting at i + 2 as well
# for example, if we have "123", we can decode "123" by splitting into "1" and "23" or "12" and "3"

# we set the value at i to the value at i + 1 plus the value at i + 2 if it exists

# finally, we return the value at 0
# we do this because the value at 0 is the number of ways to decode the entire string