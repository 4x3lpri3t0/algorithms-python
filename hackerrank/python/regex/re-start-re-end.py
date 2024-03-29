import re

string = input()
sub = input()

matches = list(re.finditer(r'(?={})'.format(sub), string))

if matches:
    for match in matches:
        print((match.start(), match.end() + len(sub) - 1))
else:
    print((-1, -1))
