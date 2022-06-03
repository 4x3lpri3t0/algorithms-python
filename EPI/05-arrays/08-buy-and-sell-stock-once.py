def get_max_profit(A: list[float]) -> float:
    max_diff = 0.0
    min_price = float("inf")

    for cur_price in A:
        min_price = min(min_price, cur_price)
        max_diff = max(max_diff, cur_price - min_price)

    return max_diff


# TC: O(n)
# SC: O(1)

A = [100, 50, 25]
max_profit = get_max_profit(A)
assert max_profit == 0

A = [0, 1000, 10]
max_profit = get_max_profit(A)
assert max_profit == 1000

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
max_profit = get_max_profit(A)
assert max_profit == 30
