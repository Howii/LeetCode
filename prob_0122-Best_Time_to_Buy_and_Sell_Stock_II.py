from typing import List

def maxProfit(prices: List[int]) -> int:
    maxprofit = 0
    for k in range(1, len(prices)):
        if prices[k] > prices[k-1]:
            maxprofit += prices[k] - prices[k-1]
    return maxprofit
