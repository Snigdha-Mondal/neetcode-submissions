class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       max_profit=0
       min_price=prices[0]

       for i in prices:
        if i<min_price:
            min_price=i
        else:
            profit=i-min_price
            max_profit=max(max_profit,profit)

       return max_profit

