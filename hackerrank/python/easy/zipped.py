N, X = map(int, input().split())
grades_by_subject = []

for _ in range(X):
    grades_by_subject.append(map(float, input().split()))

for grades_by_student in zip(*grades_by_subject):
    print(sum(grades_by_student) / len(grades_by_student))
