"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
"""

def maxProfit(prices: list[int]) -> int:
    b = 0
    s = 1
    maxProfit = 0

    while s < len(prices):
        if prices[s] > prices[b]:
            profit = prices[s] - prices[b]
            maxProfit = max(maxProfit, profit)
        else:
            b = s
        s += 1
    
    return maxProfit

print(maxProfit([2,1,2,1,0,1,2]))    
print(maxProfit([7,1,5,3,6,4]))    
print(maxProfit([7,6,4,3,1]))    
print(maxProfit([1,2]))    
print(maxProfit([1,1]))    
print(maxProfit([0,0,1]))    
print(maxProfit([2,4,1]))  