def is_palindromic(s: str) -> bool:
    # Note that s[~i] for i in [0, len(s) - 1] is s[-(i + 1)].
    return all(s[i] == s[~i] for i in range(len(s) // 2))


assert is_palindromic("aba")
assert is_palindromic("aabbaa")
assert is_palindromic("abb") == False

# Key operators and functions on strings (examples):
# s[3]
# len(s)
# s + t
# s[2:4]

# s in t
# s.strip()
# s.startswith(prefix)
# s.endswith(suffix)
# 'Euclid,Axiom 5,Parallel Lines'.split(',')
# 3 * '01'
# ','.join(('Gauss', 'Price of Mathematics', '1777-1855'))
# s.tolower()
# 'Name {name}, Rank {rank}'.format(name='Archimedes', rank=3)
