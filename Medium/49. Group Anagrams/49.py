from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for str in strs:
            newStr = ''.join(sorted(str))
            if newStr not in d:
                d[newStr] = [str]
            else:
                d[newStr].append(str)
        return d.values()

# first, create a dictionary to store the sorted strings and their anagrams
# iterate through the list of strings
# for each string, sort it and store it in a new variable
# if the sorted string is not in the dictionary, add it as a key and the original string as a value
# else, append the original string to the list of anagrams
# return the values of the dictionary