# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/submissions/
#Runtime: 1592 ms, faster than 14.11% of Python3 online submissions for Best Time to Buy and Sell Stock III.
#Memory Usage: 29.1 MB, less than 22.01% of Python3 online submissions for Best Time to Buy and Sell Stock III.

class Solution:
    def maxProfit(self,prices):
        buy_1 = [None for _ in range(len(prices))] # 第K 天持有状态下最大利润
        sell_1 =[None for _ in range(len(prices))]

        buy_2 =[None for _ in range(len(prices))]
        sell_2 = [None for _ in range(len(prices))]
        buy_1[0] = -prices[0]

        sell_1[0] = -float('inf')

        buy_2[0] = -float('inf')

        sell_2[0] = -float('inf')
        
        max_profit  = 0
        for t in range(1,len(prices)):

            buy_1[t] = max(buy_1[t-1],-prices[t]) # 第一天买入，或者之前就已经买入了
            sell_1[t] =max(sell_1[t-1],prices[t]+buy_1[t-1]) # 第K 天，卖出的最大利润， 昨天卖得多还是今天卖好

            buy_2[t] = max(buy_2[t-1],sell_1[t-1]-prices[t]) # 第K 天 第二次买入的最大利润是多少，要不昨天买入的利润大，还是今天买入的利润大

            sell_2[t] = max(sell_2[t-1],prices[t]+buy_2[t-1]) # 第K 天，今天卖出好，还是昨天卖出好 ？ 

            max_profit = max(max_profit,max(sell_1[t],sell_2[t]))
        return max_profit
    

#     Time Limit Exceeded
class Solution:
    def maxProfit(self,prices):
        buy_1 = [None for _ in range(len(prices))]
        sell_1 =[None for _ in range(len(prices))]

        buy_2 =[None for _ in range(len(prices))]
        sell_2 = [None for _ in range(len(prices))]

        buy_1[0] = -prices[0]
        max_profit = 0

        for i in range(1,len(prices)):

            buy_1[i] = -prices[i] # 当刻第一次购买

            # 第一次卖出的获利 = 之前最小的买入 + 当前的价格
            prev_buy = [price for price in buy_1[:i] if price is not None ] # <- 需要优化
            if len(prev_buy)==0:
                sell_1[i] = None
            else:
                sell_1[i] = max(prev_buy)+prices[i]
                max_profit  = max(max_profit,sell_1[i])

            # 第二次买入的话， 就是之前的卖出获利 加上此刻的成本
            prev_sell = [price for price in sell_1[:i] if price is not None]
            if len(prev_sell)==0:
                buy_2[i] =None
            else:
                buy_2[i] = -prices[i] + max(prev_sell) 

            # 第二次卖出的话，上一刻买入的最高的获利 加上此刻的成本
            prev_buy = [price for price in buy_2[:i] if price is not None]
            if len(prev_buy)==0:
                sell_2[i] = None
            else:
                sell_2[i] = max(prev_buy)+prices[i]
                max_profit  = max(max_profit,sell_2[i])
                
        return max_profit
            
    