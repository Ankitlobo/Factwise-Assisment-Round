def max_profit(prices):
    if not prices or len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

# Example usage:
prices1 = [7, 1, 5, 3, 6, 4]
print(max_profit(prices1))  # Output: 5

prices2 = [7, 6, 4, 3, 1]
print(max_profit(prices2))  # Output: 0