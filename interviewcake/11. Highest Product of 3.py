def highest_product_of_3(nums):
    highest = max(nums[0], nums[1])
    lowest = min(nums[0], nums[1])
    highest_product_of_2 = highest * lowest
    lowest_product_of_2 = highest * lowest

    # In our first pass it'll check against itself, which is fine.
    highest_product_of_3 = nums[0] * nums[1] * nums[2]

    for i in range(2, len(nums)):
        current = nums[i]
        highest_product_of_3 = max(highest_product_of_3,
                                   highest_product_of_2 * current,
                                   lowest_product_of_2 * current)
        highest_product_of_2 = max(highest_product_of_2,
                                   highest * current,
                                   lowest * current)
        lowest_product_of_2 = min(lowest_product_of_2,
                                  highest * current,
                                  lowest * current)
        highest = max(highest, current)
        lowest = min(lowest, current)
    return highest_product_of_3


list = [-10, -10, 1, 3, 2]
print(highest_product_of_3(list))
