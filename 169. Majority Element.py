# Problem: 169. Majority Element
# Difficulty: Easy

# Efficiency: O(n) time, O(n) space

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        i = 0
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1  
        for key, value in count.items():
            if value > len(nums)/2:
                print(key, "->", value)
                return key
        