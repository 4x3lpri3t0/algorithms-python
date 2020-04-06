# https://www.interviewcake.com/question/python3/merge-sorted-arrays
def merge_lists(a_list, b_list):
    a_index, b_index = 0, 0
    merged_list = []
    while a_index < len(a_list) and b_index < len(b_list):
        if a_list[a_index] < b_list[b_index]:
            merged_list.append(a_list[a_index])
            a_index += 1
        else:
            merged_list.append(b_list[b_index])
            b_index += 1
    while a_index < len(a_list):
        merged_list.append(a_list[a_index])
        a_index += 1
    while b_index < len(b_list):
        merged_list.append(b_list[b_index])
        b_index += 1
    return merged_list


my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
