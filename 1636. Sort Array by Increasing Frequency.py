# Time Complexity: O(nlogn)
# Space Complexity: O(n)

# Approach:
# 1. We will first sort the array in decreasing order.
# 2. We will then sort the array based on the frequency of the elements.
# 3. We will return the result.


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums,reverse=True)
        result = sorted(sorted_nums, key=nums.count)
        return result