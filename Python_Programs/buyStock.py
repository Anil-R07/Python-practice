'''Best Time to Buy and Sell Stock.
👉 Goal:
Find the maximum profit you can make by buying one day and selling later'''

def maxProfit(prices):
    minPrice = float('inf')
    profit = 0
    for price in prices:
        if price < minPrice:
            minPrice  = price
        currentProfit = price - minPrice

        if currentProfit > profit:
            profit = currentProfit
    return profit
max_Profit = maxProfit([1, 3, 10, 5, 4])
print(max_Profit)

# one more way 

def findProfit(prices):
    min_price = float('inf')
    profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price )
    return profit 
max_profit = findProfit([1, 3, 10, 5, 4])
print(max_profit)
