class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        totalOnes = sum(nums)
        length = len(nums)
        minSwaps = currentSwaps = totalOnes - sum(nums[:totalOnes])
        for i in range(totalOnes, length + totalOnes):
            currentSwaps += nums[i - totalOnes] - nums[i % length]
            minSwaps = min(currentSwaps, minSwaps)
        return minSwaps