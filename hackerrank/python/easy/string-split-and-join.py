def split_and_join(line):
    splitted = line.split(" ")
    return "-".join(splitted)


line = input()
result = split_and_join(line)
print(result)