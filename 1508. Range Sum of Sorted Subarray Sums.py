def mod_10_9_plus_7(n):
    MOD = 10**9 + 7
    return n % MOD

class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(len(nums)):
            sum = nums[i]
            res.append(sum)
            j = i + 1
            while j < len(nums):
                sum = sum + nums[j]
                res.append(sum)
                j += 1
        res.sort()
        res_sum = 0
        left = left - 1
        right = right - 1
        while(left < len(res) and left <= right):
            res_sum += res[left]
            left = left + 1
        return mod_10_9_plus_7(res_sum)
