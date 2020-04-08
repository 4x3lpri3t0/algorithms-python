def get_max_profit(stocks):
    total_profit = 0
    for i in range(1, len(stocks)):
        # Buy previous?
        if stocks[i] > stocks[i - 1]:
            total_profit += (stocks[i] - stocks[i - 1])
    return total_profit


print(get_max_profit([10, 7, 5, 8, 11, 9]))  # 6
print(get_max_profit([0, 1, 2]))  # 2
print(get_max_profit([1, 2, 10]))  # 9
