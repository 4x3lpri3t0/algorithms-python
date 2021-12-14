import re

# Can't use '\w' since we don't want to match an underscore
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)