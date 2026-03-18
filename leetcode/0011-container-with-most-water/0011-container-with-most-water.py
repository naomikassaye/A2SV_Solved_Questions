class Solution:
    def maxArea(self, height: list[int]) -> int:
        left, right = 0, len(height) - 1
        maxarea = 0

        while left < right:
            width = right - left
            maxarea = max(maxarea, min(height[left], height[right]) * width)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxarea