class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        l, r = 0, len(nums) - 1
        while r - l != 1:
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid
        return min(nums[r], nums[l])