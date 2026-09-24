from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        for num, freq in freq_map.items():
            x = (freq, num)
            heapq.heappush(heap, x)
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]