from typing import Callable, List, Tuple
def bsearch(t: int, A: List[int]) -> int:
    L, U = 0, len(A) - 1
    while L <= U:
        M = (L + U) // 2
        if A[M] < t:
            return M
        else:
            U = M - 1
    return -1
# To avoid a potential overflow, better use:
# M = L + (U - L) / 2


# Using Python's BS routine:
import collections
import bisect
Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def comp_gpa(student: Student) -> Tuple[float, str]:
    return (-student.grade_point_average, student.name)

def search_student(students: List[Student], target: Student, comp_gpa: Callable[[Student], Tuple[float, str]]):
    i = bisect.bisect_left([comp_gpa(s) for s in students], comp_gpa(target))
    return 0 <= i < len(students) and students[i] == target

# To find the first element that is not less than a targeted value:
# bisect.bisect_left(a, x)
# ...                               greater than ...              :
# bisect.bisect_right(a, x)