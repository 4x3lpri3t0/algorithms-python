import sys

M = [list(map(int, a.strip().split())) for a in sys.stdin.readlines()]
N = [[1 for _ in range(len(M[0]))] for _ in range(len(M))]


def change(N, i, j):
    N[i][j] = 0 if N[i][j] == 1 else 1


for i in range(len(M)):
    for j in range(len(M[i])):
        if M[i][j] % 2:
            change(N, i, j)

            if i > 0:
                change(N, i - 1, j)
            if i < len(M) - 1:
                change(N, i + 1, j)
            if j > 0:
                change(N, i, j - 1)
            if j < len(M[i]) - 1:
                change(N, i, j + 1)

for row in N:
    print(''.join(map(str, row)))