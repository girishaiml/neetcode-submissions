import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert the stones into a max heap using negative values
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = -heapq.heappop(stones)   # Heaviest stone
            second = -heapq.heappop(stones)  # Second-heaviest stone

            if first != second:
                heapq.heappush(stones, -(first - second))

        return -stones[0] if stones else 0