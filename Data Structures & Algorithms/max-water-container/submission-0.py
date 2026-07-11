class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            width = right - left
            container_height = min(heights[left], heights[right])
            max_water = max(max_water, width * container_height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_water