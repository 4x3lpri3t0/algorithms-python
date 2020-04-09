# Pigeonhole Principle + BS
def find_repeat(numbers):
    floor = 1
    ceiling = len(numbers) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_floor, lower_ceiling = floor, midpoint
        upper_floor, upper_ceiling = midpoint+1, ceiling

        # Count number of items in lower range
        items_in_lower = 0
        for item in numbers:
            # Is it in the lower range?
            if item >= lower_floor and item <= lower_ceiling:
                items_in_lower += 1

        distinct_possible_integers_in_half = (
            lower_ceiling
            - lower_floor
            + 1
        )
        if items_in_lower > distinct_possible_integers_in_half:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_floor, lower_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_floor, upper_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor


print(find_repeat([1, 2, 3, 4, 1, 5, 6]))  # 1
