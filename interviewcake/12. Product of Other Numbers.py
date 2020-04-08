def get_products_of_all_ints_except_at_index(nums):
    result = [None] * len(nums)

    product_so_far = 1
    for i in range(len(nums)):
        result[i] = product_so_far
        product_so_far *= nums[i]

    product_so_far = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= product_so_far
        product_so_far *= nums[i]

    return result


print(get_products_of_all_ints_except_at_index([1, 7, 3, 4]))
