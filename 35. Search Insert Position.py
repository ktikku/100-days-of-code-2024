# Time Complexity: O(log(n))
# Space Complexity: O(log(n))
# Recursive Solution

#  This is a recursive solution. We find the middle element of the list and check if it is the target. If it is we return the element.
#  If the middle element is greater than the target we recursively call the function with the first half of the list. If the middle element
#  is less than the target we recursively call the function with the second half of the list. We return the element that is closest to the target.
#  If the element is greater than the target we return the element. If the element is less than the target we return the element after the element.
#  If the element is equal to the target we return the index of the element.

def find_element(nums, target):
    length = len(nums)
    mid = (length // 2) - 1
    if length == 1 or nums[mid] == target:
        return nums[mid]
    return find_element(nums[:mid+1], target) if nums[mid] > target else find_element(nums[mid+1:], target)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        element = find_element(nums, target)
        if element == target:
            return nums.index(target)
        elif element > target:
            return nums.index(element)
        elif element < target:
            return nums.index(element) + 1
