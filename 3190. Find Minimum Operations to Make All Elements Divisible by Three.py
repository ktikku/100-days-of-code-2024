class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        for num in nums:
            remainder = num % 3
            if remainder == 1:
                operations += 1
            elif remainder == 2:
                operations += 1
        return operations