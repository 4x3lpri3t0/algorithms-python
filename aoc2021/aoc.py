import re
import os

# Most of this is shamelessly stolen.

cat = ''.join
inf = float('inf')


def mapl(f, iterable):
    return list(map(f, iterable))

def mapt(f, iterable):
    return tuple(map(f, iterable))

def read_input(filename, datatype=str, sep='\n'):
    filename = f"{filename:02d}" if isinstance(filename, int) else filename
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = os.path.join("inputs", f"{filename}.txt")
    abs_file_path = os.path.join(script_dir, rel_path)
    with open(abs_file_path) as f:
        contents = f.read().strip().split(sep)
        return mapl(datatype, contents)

def read_input_line(filename, datatype=str, sep=' '):
    return read_input(filename, datatype=datatype, sep=sep)

def digits(line):
    return mapt(int, line)

def integers(text, negative=True):
    return mapt(int, re.findall(r"-?\d+" if negative else r"\d+", text))

def count(iterable, pred=bool):
    return sum(1 for item in iterable if pred(item))

def first(iterable, default=None):
    return next(iter(iterable), default)

def filter_first(iterable, pred):
    return first(el for el in iterable if pred(el))

def manhattan(a, b = (0, 0)) -> int:
    return sum(abs(p - q) for p, q in zip(a, b))

def sign(n):
    if n > 0: return 1
    elif n < 0: return -1
    else: return 0

def line_print(lines):
    for line in lines:
        print(cat(line))

def maxval(d):
    return max(d.values())

def transpose(matrix):
    return list(zip(*matrix))

def bin2int(s):
    return int(s, 2)


if __name__ == "__main__":
    assert cat(["ab", "cd", "ef"]) == "abcdef"
    assert mapl(int, ["1", "2"]) == [1, 2]
    assert mapt(int, ["1", "2"]) == (1, 2)
    assert digits("123") == (1, 2, 3)
    assert integers("23 -42 55") == (23, -42, 55)
    assert integers("23 -42 55", negative=False) == (23, 42, 55)
    assert count([3, -5, 10, -7, 33], lambda x: x > 0) == 3
    assert first([2, 4, 6, 8]) == 2
    assert filter_first([2, 7, 4, 6, 8], lambda x: x > 5) == 7
    assert manhattan((5, -3)) == 8
    assert manhattan((5, -3), (2, 7)) == 13
    assert maxval(dict(a=3, b=99, c=66)) == 99