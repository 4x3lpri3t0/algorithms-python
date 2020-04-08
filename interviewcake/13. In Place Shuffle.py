# Fisher-Yates shuffle
import random


def get_random(floor, ceiling):
    return random.randrange(floor, ceiling + 1)


def shuffle(list):
    if len(list) <= 1:
        return list

    last_idx = len(list) - 1
    # Walk through from beginning to end
    for current_idx in range(0, last_idx):

        # Choose a random not-yet-placed item to place there
        # (could also be the item currently in that spot)
        # Must be an item AFTER the current item, because the stuff
        # before has all already been placed
        random_idx = get_random(current_idx, last_idx)

        # Swap!
        list[current_idx], list[random_idx] = list[random_idx], list[current_idx]


nums = [3, 1, 64, 2, 100]
shuffle(nums)
print(nums)
