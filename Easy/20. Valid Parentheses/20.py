from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        parMap = {"(": ")", "[": "]", "{": "}"}
        
        for ch in s:
            if ch in parMap:
                stack.append(parMap[ch])
            elif not stack or stack.pop() != ch:
                return False
        
        return not stack

# first, create a stack
# create a dictionary to store the matching parentheses
# iterate through each character in the string
# if the character is an opening parenthesis
# append the matching closing parenthesis to the stack
# else if the stack is empty or the top of the stack does not match the current character
# return false
# return whether the stirng is empty or not