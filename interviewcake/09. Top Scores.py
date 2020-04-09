from collections import defaultdict


def def_sort_scores_array(unsorted_scores, highest_possible_score):
    # List of 0s at indices 0..highest_possible_score
    score_counts = [0] * (highest_possible_score+1)

    # Populate score_counts
    for score in unsorted_scores:
        score_counts[score] += 1

    # Populate the final sorted list
    sorted_scores = []
    for score in range(len(score_counts) - 1, -1, -1):
        count = score_counts[score]

        # For the number of times the item occurs
        for time in range(count):
            sorted_scores.append(score)

    return sorted_scores


def sort_scores_dict(scores, HIGHEST_POSSIBLE_SCORE):
    sorted_list = []
    dict = defaultdict(list)
    for score in scores:
        dict[score].append(score)

    for key in reversed(range(HIGHEST_POSSIBLE_SCORE)):
        if key in dict.keys():
            for time in dict[key]:
                # Number may have appeared multiple times
                sorted_list.append(time)

    return sorted_list


unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

# Returns [91, 89, 65, 53, 41, 37]
print(sort_scores_dict(unsorted_scores, HIGHEST_POSSIBLE_SCORE))

print(sort_scores_dict([1, 2, 1, 2, 5, 3], 10))
