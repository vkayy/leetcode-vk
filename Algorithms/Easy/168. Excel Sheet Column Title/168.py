class Solution:
  def convertToTitle(self, columnNumber: int) -> str:
    return chr(columnNumber + 64) if 0 < columnNumber < 27 else (self.convertToTitle(columnNumber // 26) + chr((columnNumber % 26) + 64)) if columnNumber % 26 else (self.convertToTitle(columnNumber // 26 - 1) + 'Z')

# if the number is between 1 and 26, return the corresponding letter
# otherwise, if the number is not divisible by 26, return the letter corresponding to the remainder and the letter corresponding to the quotient
# otherwise, if not, return the letter corresponding to the quotient minus 1 and 'Z'
# we take away 1 and use Z as there is no 0 in the alphabet
