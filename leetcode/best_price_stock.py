#class Solution:
#    def maxProfit(self, prices: List[int]) -> int:
#        price_min = 0
#        # price_max = 0
#        price_delta_max = 0
#        for index, price in enumerate(prices):
#            price_delta = 0
#            if price < price_min or index == 0:
#                price_min = price
#            price_delta = price - price_min
#            if price_delta > price_delta_max:
#                price_delta_max = price_delta
#        return price_delta_max
# 6ms faster
# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         price_min = prices[0]
#         price_max = 0
        # price_delta_max = 0
        # for price in prices:
        #     price_delta = 0
        #     if price < price_min or index == 0:
        #         price_min = price
        #     price_delta = price - price_min
        #     if price_delta > price_delta_max:
        #         price_delta_max = price_delta
        # return price_delta_max

