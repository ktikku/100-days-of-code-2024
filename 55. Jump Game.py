# Wrong Solution 
# 52 / 172 testcases passed

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i, can_jump = 0,False
        if nums[0] == 0 and len(nums) == 1:
            return True
        if nums[0] == 1 and len(nums) == 1:
            return True
        for i in range(len(nums) - 1):
            j = i;
            jumps = len(nums) - j - 1
            while j < len(nums) - 1:
                if nums[j] == 0:
                    break
                print('jumps before', jumps, j)
                jumps -= nums[j]
                j += nums[j]
                print('jumps', jumps, j)
                if jumps == 0:
                    can_jump = True
                    break
            if jumps == 0:
                can_jump = True
                break
        return can_jump

# Correct Solution
# 172 / 172 testcases passed.
# Greedy Solution

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        if goal == 0:
            return True
        return False
# Explanation: Start from the end and shift the goal to the left if the current index can reach the goal. If the goal is 0, then we can reach the end. Otherwise, we can't reach the end.

