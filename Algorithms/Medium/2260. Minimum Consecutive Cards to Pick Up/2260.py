from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        lst, mn = {}, float("inf")
        for idx, card in enumerate(cards):
            if card in lst and (new := idx - lst[card] + 1) < mn:
                mn = new
            lst[card] = idx
        return mn if mn != float("inf") else -1

# first, we can create a dictionary to keep track of the last index of each card
# then, we can iterate through the array

# if the current card is in the dict, find the difference between the current index and the last index of the card
# if the difference is less than the minimum, update the minimum
# this is because we can pick up the cards between the last index and the current index, inclusive

# then, we can update the last index of the card to the current index

# then, we can return the minimum if it is not infinity, else return -1
# i.e., if we found a pair of cards, return the minimum, else return -1