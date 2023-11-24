from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        mostFreqK = freqs.most_common(k)
        result = []
        for i in range(k):
            result.append(mostFreqK[i][0])
        return result

# create a dictionary of frequencies
# select the k most frequent key-value pairs
# extract the keys and return them as a list