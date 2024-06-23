# Time complexity: O(n)
# Space complexity: O(n)
# Hash Map Solution

from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = defaultdict(int)

        for i in range(len(nums)):
            nums_map[nums[i]] = i
        
        for i in range(len(nums)):
            if nums_map.get(target - nums[i]) and i !=  nums_map.get(target - nums[i]):
                return [i, nums_map.get(target - nums[i])]
        