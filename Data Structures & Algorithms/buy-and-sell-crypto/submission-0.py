class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        current_max =0
        buy_price = prices[0]
        for item in prices:
            current_max = max(current_max,item -buy_price)
            if buy_price> item:
                buy_price = item
        return current_max

        