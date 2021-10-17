from typing import List

def maxProfit(prices: List[int]) -> int:
    '''
    Let a[k] be the highest profit if sell at p[k], then we have recursion
    a[k] = max(0, a[k-1] + p[k] - p[k-1])
    '''
    top = a = 0
    for k in range(1, len(prices)):
        a = max(0, a + prices[k] - prices[k-1])
        if a > top:
            top = a
    return top
