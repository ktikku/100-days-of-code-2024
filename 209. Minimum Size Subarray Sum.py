import sys
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = 0
        l = 0
        r = 0
        max_len = sys.maxsize
        while r < len(nums):
            sum = nums[r] + sum
            if sum < target:
                r += 1
            else:
                max_len = min(max_len, r - l + 1)
                sum = sum - nums[r]
                sum = sum - nums[l]
                l += 1  
        if max_len < sys.maxsize:
            return max_len
        else:
            return 0