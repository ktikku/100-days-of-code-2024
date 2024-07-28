# Time Complexity: O(n^2)
# Space Complexity: O(n)

# Approach: 
# Sort the array and then iterate through the array. 
# For each element, we will find the two elements that sum up to the negative of the current element. 
# We will use two pointers to find the two elements. 
# If the sum is greater than 0, we will decrement the right pointer. 
# If the sum is less than 0, we will increment the left pointer.
# If the sum is 0, we will add the three elements to the result and then increment the left pointer. 
# We will also skip the duplicates by checking if the current element is the same as the previous element.

from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        l, r = 0, 0
        res = []
        for i in range(len(nums) - 2):
            if i > 0:
                if nums[i] == nums[i - 1]:
                    continue
            if nums[i] > 0:
                break
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = nums[l] + nums[r] + nums[i]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
            
            