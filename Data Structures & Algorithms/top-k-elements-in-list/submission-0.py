from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        topK_freq = freq.most_common(k)
        topK = []
        for pair in topK_freq:
            topK.append(pair[0])
        return topK