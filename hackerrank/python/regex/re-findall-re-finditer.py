## re.findall(): returns all the non-overlapping matches of patterns in a string as a list of strings.
# >>> re.findall(r'\w','http://www.hackerrank.com/')
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

## re.finditer(): returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.
# >>> re.finditer(r'\w','http://www.hackerrank.com/')
# <callable-iterator object at 0x0266C790>
# >>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
# ['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

import re

s = input()
regexp = re.compile(r'(?<=[^aeiou])[aeiou]{2,}(?=[^aeiou])',
                    flags=re.IGNORECASE)
m = re.findall(regexp, s)

[print(i) for i in m] if m else print("-1")
