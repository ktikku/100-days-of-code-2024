def binary_search(l, r, nums, target):
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        l = 0
        r = len(nums) - 1
        pivot = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if mid > 0 and nums[mid - 1] > nums[mid]:
                pivot = mid
                break
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid - 1
        if target == nums[pivot]:
            return pivot 
        if target >= nums[0]:
            l = 0
            r = pivot
            return binary_search(l, r, nums, target)
        if target < nums[0]:
            l = pivot + 1
            r = len(nums) - 1
            return binary_search(l, r, nums, target)
        return -1