# https://www.interviewcake.com/question/python3/merging-ranges
def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)  # key=lambda x: x[0] not needed here

    # Initialize merged_meetings with the earliest meeting
    merged_meetings = [sorted_meetings[0]]

    for current_start, current_end in sorted_meetings[1:]:
        last_start, last_end = merged_meetings[-1]  # Get last ones

        if (current_start <= last_end):
            # Merge last tuple with current
            merged_meetings[-1] = (last_start,
                                   max(last_end, current_end))
        else:  # They don't overlap
            merged_meetings.append((current_start, current_end))
    return merged_meetings


print(merge_ranges([[0, 1], [8, 9], [1, 2]]))
print(merge_ranges([[0, 1], [1, 2], [0, 3], [0, 10]]))
