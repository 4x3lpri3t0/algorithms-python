import numpy

if numpy.version.version >= '1.14.':
    numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], float)

print(numpy.mean(a, axis=1))
print(numpy.var(a, axis=0))
print(numpy.around(numpy.std(a), 12))