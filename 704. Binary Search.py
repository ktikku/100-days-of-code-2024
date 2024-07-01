# Time Complexity: O(log(n))
# Space Complexity: O(1)

def binary_search(l: int, r: int, target: int, nums: List[int]):
    if r >= l:
        mid = (r + l) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return binary_search(mid + 1, r, target, nums)
        else:
            return binary_search(l, mid - 1, target, nums)
    return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        result = binary_search(l, r, target, nums)
        return result