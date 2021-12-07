n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name, scores = line[0], line[1:]
    scores = map(float, scores)
    student_marks[name] = scores
query_name = input()

total_mark_sum = 0
marks_len = len(student_marks[query_name])
for mark in student_marks[query_name]:
    total_mark_sum += mark
average = total_mark_sum / marks_len
formatted_string = "{:.2f}".format(average)
print(formatted_string)