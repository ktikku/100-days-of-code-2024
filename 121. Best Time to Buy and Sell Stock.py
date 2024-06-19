# Brute Force
# Time: O(n^2)
# Space: O(1)
# 198/212 test cases passed

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, i, j = 0, 0, 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_profit = max(prices[j] - prices[i], max_profit)
        return max_profit


# One Pass
# Time: O(n)
# Space: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, i, l, r = 0, 0, 0, 1
        while(r < len(prices)):
            profit = prices[r] - prices[l]
            if(profit <= 0):
                l = r
                r += 1
                continue
            max_profit = max(profit, max_profit)
            r += 1
        return max_profit