from collections import Counter


def sherlock_and_anagrams(s):
    anagrams = 0
    c = Counter()

    for i in range(len(s)):
        combos = ["".join(sorted(s[j:j+i+1])) for j in range(len(s) - i)]
        c.update(combos)

    for k in c:
        anagrams += (c[k] - 1) * c[k] // 2

    return anagrams
