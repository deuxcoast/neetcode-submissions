from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        topK = freq.most_common(k)

        return [x[0] for x in topK]
        