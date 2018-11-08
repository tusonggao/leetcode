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