from typing import List

class Solution:
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    res, line, cur = [], [], 0
    for w in words:
      if cur + len(w) + len(line) > maxWidth:
        for i in range(maxWidth - cur):
          line[i % (len(line) - 1 or 1)] += " "
        res.append("".join(line))
        line, cur = [], 0
      line.append(w)
      cur += len(w)
    return res + [" ".join(line).ljust(maxWidth)]

# first, we initialise the result list, the current line list, and the current length

# then we iterate through the words

# if current char count + space count ((cur + len(line) - 1) + (len(w) + 1)) is greater than the max width
# we add spaces to the line to justify the text

# for ech space, we add a space to the word at the current index % (len(line) - 1 or 1)
# this is because we want to evenly distribute the spaces between the words, but if there is only one word, we add a space to the word
# then we append the line to the result list
# and reset the line and current length

# we then append the word to the line and add the length of the word to the current length

# then, we return the result list with the last line left-justified
