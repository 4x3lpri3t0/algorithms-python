from collections import defaultdict


def sort_scores(scores, HIGHEST_POSSIBLE_SCORE):
    sorted_list = []
    map = defaultdict(list)
    for score in scores:
        map[score].append(score)

    for key in reversed(range(HIGHEST_POSSIBLE_SCORE)):
        if key in map.keys():
            for time in map[key]:
                # Number may have appeared multiple times
                sorted_list.append(time)

    return sorted_list


unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))

print(sort_scores([1, 2, 1, 2, 5, 3], 10))
