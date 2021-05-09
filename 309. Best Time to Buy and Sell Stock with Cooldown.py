#https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/submissions/
#Runtime: 36 ms, faster than 84.26% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
#Memory Usage: 14.8 MB, less than 23.37% of Python3 online submissions for Best Time to Buy and Sell Stock with Cooldown.
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hold [i] 第i天持有股票的利润
        #unhold [i] 第i天不持有股票的利润
        
        n = len(prices)
        if n<2:
            return 0
        
        hold = [None for _ in range(n)]
        unhold = [None for _ in range(n)]
        
        hold[0] = -prices[0] #持有股票当天花费的费用
        
        # 一天还持有股票的profit i) 之前没有持有现在持有，2）之前持有，现在也没有卖/ 没有卖就没有产生profit 
        hold[1] =  max(-prices[1],-prices[0]) # 看看第一天产生的成本那个比较低
        
        unhold[0] = 0
        
        for i in range(1,n):
            if i >1:
                # 第三天持有股票的profit，1) 之前没有持有股票，现在持有（之前没有持有股票的价格-当前成本）， 2）之前持有，现在还在持有
                hold[i] =  max(unhold[i-2]-prices[i],hold[i-1])
            
            # 第三天不持有股票的 profit  1）当天没有卖出股票 2）现在卖掉股票
            unhold[i]= max(unhold[i-1],hold[i]+prices[i])
        
        return unhold[n-1] # 最后一天不持有股票