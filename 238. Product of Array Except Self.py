# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: 
# 1. We will first calculate the prefix product of the array.
# 2. Then we will calculate the postfix product of the array.
# 3. The product of prefix and postfix at each index will give the result.
# 4. We will return the result.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix = postfix * nums[i]
        return res