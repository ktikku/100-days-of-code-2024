# Time complexity: O(nlogn)
# Space complexity: O(1)

# This is a binary search solution. We iterate through the list of numbers and for each number we find the 
# difference between the target and the number. We then perform a binary search on the list of numbers to
# find the difference. If we find the difference we return the indices of the two numbers. If we don't find
# the difference we continue to the next number. If we reach the end of the list we return None.

def binarySearch(low: int, high: int, diff: int, numbers: List[int]) -> int:
    if high >= low:
        mid = (high + low) // 2
        if numbers[mid] == diff:
            return mid
        elif numbers[mid] > diff:
            return binarySearch(low, mid - 1, diff, numbers)
        else:
            return binarySearch(mid + 1, high, diff, numbers)
    return None

class Solution:    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            diff = (target - numbers[i])
            index = binarySearch(0, len(numbers) - 1, diff, numbers)
            print(i, index)
            if index is not None and i != index:
                return sorted([i + 1, index + 1])
            continue