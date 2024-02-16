from typing import List
from collections import defaultdict, deque

class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    n = len(beginWord)
    adj = defaultdict(list)
    for w in wordList:
      for i in range(n):
        adj[w[:i] + '#' + w[i + 1:]].append(w)
    q = deque([(beginWord, 1)])
    v = set([beginWord])
    while q:
      cur, lvl = q.popleft()
      for i in range(n):
        bridge = cur[:i] + '#' + cur[i + 1:]
        for w in adj[bridge]:
          if w == endWord:
            return lvl + 1
          if w not in v:
            v.add(w)
            q.append((w, lvl + 1))
    return 0

# first, we create an adjacency list for the word list
# then we use breadth-first search to find the shortest transformation sequence
# if we find the end word, we return the length of the sequence
# if we do not find the end word, we return 0
# this is because we cannot transform the begin word into the end word
# therefore, the result is 0

# we initialise the adjacency list by iterating through the word list
# for each word, we iterate through the characters and replace each character with a wildcard
# we then append the word to any possible wildcard of the word

# we initialise a queue with the begin word and the level of the sequence
# we initialise a set with the begin word for visited words

# we then perform breadth-first search
# at each step, we pop the first word from the queue
# we iterate through the characters of the word
# we replace each character with a wildcard
# for each wildcard, we iterate through the words in the adjacency list
# if we find the end word, we return the length of the sequence
# if we do not find the end word, we add the word to the visited set and append the word to the queue
# finally, we return 0 if we do not find the end word
