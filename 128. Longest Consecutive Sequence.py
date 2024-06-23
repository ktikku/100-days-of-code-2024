# Brute force solution
# Space complexity: O(n)
# Hash Map Solution
# 69/76 test cases passed
# TLE

from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_map = defaultdict(int)
        for i in range(len(nums)):
            nums_map[nums[i]] = nums[i]
        keys = nums_map.keys()
        keys_list = list(keys)
        max_count = 0
        for i in range(len(keys_list)):
            count = 1
            start = keys_list[i]
            while nums_map.get(start + 1) != None:
                count += 1
                start += 1
            max_count = max(count, max_count)
        return max_count

# Time complexity: O(n)
# Space complexity: O(n)
# Hash Map Solution

from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_map = defaultdict(int)
        for i in range(len(nums)):
            nums_map[nums[i]] = nums[i]
        keys = nums_map.keys()
        keys_list = list(keys)
        max_count = 0
        for i in range(len(keys_list)):
            if nums_map.get(keys_list[i] - 1) != None:
                continue
            count = 1
            start = keys_list[i]
            while nums_map.get(start + 1) != None:
                count += 1
                start += 1
            max_count = max(count, max_count)
        return max_count