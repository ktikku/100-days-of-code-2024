# Time: O(n) - one pass
# Space: O(1) - only use constant space

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, max_area = 0, len(height) - 1, 0
        while l < r:
            max_area = max((r - l) * min(height[l], height[r]), max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1                     
        return max_area
        