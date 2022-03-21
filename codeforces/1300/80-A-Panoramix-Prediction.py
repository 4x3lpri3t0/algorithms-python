n, m = map(int, input().split())
next_prime = n + 1


def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


# Get next prime from n
while not is_prime(next_prime) and next_prime <= m:
    next_prime += 1

print("YES" if next_prime == m else "NO")