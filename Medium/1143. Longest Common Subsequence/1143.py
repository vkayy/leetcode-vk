class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        T1, T2 = len(text1), len(text2)
        
        dp = [[0] * (T2 + 1) for _ in range(T1 + 1)]
        
        for i in range(T1 - 1, -1, -1):
            
            for j in range(T2 - 1, -1, -1):
                
                if text1[i] == text2[j]:
                    
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                
                else:
                    
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
                
        return dp[0][0]

# first, we create variables T1 and T2 and set them to the lengths of text1 and text2

# then, we create a 2d array called dp, filled with 0s
# we extend the length of the rows and columns by 1 to account for the empty string

# then, we iterate through the rows backwards
# this is because our recurrence relation depends on the row below the current row
# this also enables later subsequences to be filled before earlier

# then, we iterate through the columns backwards
# this is because our recurrence relation depends on the column to the right of the current column
# this also enables later subsequences to be filled before earlier
 
# if the characters at i and j are the same
# we set the value at i and j to 1 plus the value at i + 1 and j + 1
# this is because we can add the character at i to the longest common subsequence of the substrings starting at i + 1 and j + 1

# otherwise, we set the value at i and j to the maximum of the value at i + 1 and j and the value at i and j + 1
# this is because we can take the longest common subsequence of the substrings starting at i + 1 and j or the substrings starting at i and j + 1

# finally, we return the value at 0 and 0
# this is because the value at 0 and 0 is the longest common subsequence of the entire strings