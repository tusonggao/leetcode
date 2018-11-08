######################################################################################
#自己花很多时间得到的解法

class Solution:
    def compute_head_profit(self, prices):
        max_profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if (prices[i] - min_price) > max_profit:
                max_profit = prices[i] - min_price
            self.head_profit.append(max_profit)
            if prices[i] < min_price:
                min_price = prices[i]
        return
    
    def compute_tail_profit(self, prices):
        max_profit = 0
        max_price = float('-inf')
        for i in range(len(prices)-1, -1, -1):
            if (max_price - prices[i]) > max_profit:
                max_profit = max_price - prices[i]
            self.tail_profit.append(max_profit)
            if prices[i] > max_price:
                max_price = prices[i]        
        self.tail_profit.reverse()
        return
        
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        self.head_profit = []
        self.tail_profit = []
        self.compute_head_profit(prices)
        self.compute_tail_profit(prices)
        
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, self.head_profit[i]+self.tail_profit[i])
        
        return max_profit
		
		
		
######################################################################################
#看到的时间效率很高的解法，目前还没有看懂。。。

class Solution:
    def maxProfit(self, prices):
        a1,a2=-10000,-10000
        b1,b2=0,0
        for o in prices:
            if a1<-o:a1=-o
            if b1<o+a1:b1=o+a1
            if a2<b1-o: a2=b1-o
            if b2<a2+o:b2=a2+o
        return b2