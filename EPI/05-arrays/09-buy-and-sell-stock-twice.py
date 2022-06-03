def get_max_profit(prices: list[float]) -> float:
    max_total_profit, min_price_so_far = 0.0, float("inf")
    first_buy_sell_profits = [0.0] * len(prices)

    # Forward phase.
    # Record max profit if we sell on that day.
    for i, price in enumerate(prices):
        min_price_so_far = min(min_price_so_far, price)
        max_total_profit = max(max_total_profit, price - min_price_so_far)
        first_buy_sell_profits[i] = max_total_profit

    # Backward phase.
    # Find the max profit if we make the second buy on that day.
    max_price_so_far = float("-inf")
    for i, price in reversed(list(enumerate(prices[1:]))):
        max_price_so_far = max(max_price_so_far, price)
        max_total_profit = max(
            max_total_profit, max_price_so_far - price + first_buy_sell_profits[i]
        )

    return max_total_profit


# TC: O(n)
# SC: O(1)

# TODO: Solve in O(n) time and O(1) space.


A = [5, 10, 5, 10]
max_profit = get_max_profit(A)
assert max_profit == 10
