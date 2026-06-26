from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return [num for num, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]