# Time Complexity: O(n)
# Space Complexity: O(n)

# Approach: Create a hashmap of the frequency of each number. 
# For each number, check if the target number is present in the hashmap. 
# If yes, decrement the frequency of both the numbers and increment the count. 
# Return the count at the end.

from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums_map = defaultdict(int)
        count = 0
        for num in nums:
            nums_map[num] += 1
        for num in nums:
            target = k - num
            if nums_map[num] > 0 and nums_map[target] > 0:
                if num == target and nums_map[num] < 2:
                    continue
                nums_map[num] -= 1
                nums_map[target] -= 1
                count += 1
        return count