# NOTE: Using numpy.
#> pip3.7 install numpy
import numpy

raw_input = list(map(int, input().split(" ")))

arr = []
for i in range(raw_input[0]):
    raw_arr = list(map(int, input().split(" ")))
    arr.append(raw_arr)

min_axis = numpy.min(arr, axis=1)
print(max(min_axis))