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

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_amount = 0
        i = 0
        j = len(heights) - 1

        while(i < j):
            max_amount = max(max_amount, min(heights[i], heights[j]) * (j - i))
            if heights[i] >= heights[j]:
                j -= 1
            else:
                i += 1
        return max_amount
        