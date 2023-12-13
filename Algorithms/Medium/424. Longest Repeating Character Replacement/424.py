class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        count = {}
        
        l = 0
        maxf = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                
            longest = max(longest, r - l + 1)
            
        return longest

# first, set the longest substring to zero
# create a dictionary to store the count of each character
# set the left pointer to zero
# set the max frequency to zero

# iterate through each index as a right pointer
# increment the count of the current character
# set the max frequency to the max of the max frequency and the incremented character count

# while the length of the substring minus the max frequency is greater than k
# decrement the count of the left character
# increment the left pointer

# set the longest substring to the max of the longest substring and the length of the substring
# return the longest substring