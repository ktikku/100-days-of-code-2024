class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, max_profit, buy, sell = 0, 0, 0, 0
        while i < len(prices) - 1:
            if(prices[i] < prices[i+1]):
                buy = prices[i]
                print('buy', prices[i])
                while prices[i] <= buy:
                    i += 1
                    print('sell', prices[i])
                sell = prices[i]
                max_profit = max_profit + sell - buy
                print(max_profit)
            else:
                i += 1
        return max_profit
