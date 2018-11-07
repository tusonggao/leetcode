#解法一

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """因为没有买卖次数限制，也没有买卖时间限制，如果后面的股价比前面的大，我们就买卖"""
        ans = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                ans += prices[i]-prices[i-1]
        return ans
		
		
####################################################################################

		
#解法二		
		
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 使用贪心算法
        if len(prices) <= 1:
            return 0
        
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i-1] >= prices[i]:
                if prices[i-1] > min_price:
                    max_profit += prices[i-1] - min_price
                min_price = prices[i]
        
        if prices[-1] > min_price:
            max_profit += prices[-1] - min_price
                
        return max_profit