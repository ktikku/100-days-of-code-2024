# Time Complexity: O(nlogn)
# Space Complexity: O(n)

def merge_sort(arr):
    # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        sorted_arr = merge_sort(nums)
        return sorted_arr

        