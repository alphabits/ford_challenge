import os

from src.utils import get_path


sess_root = get_path(__file__) + '/..'

lines = []
for f in os.listdir(sess_root):
    if f[0]=='t':
        (t_str, ext) = f.split('.')
        lines.append(t_str)

def my_sort(first, last):
    first = int(first[1:])
    last = int(last[1:])
    return -1 if first < last else (0 if first == last else 1)

lines.sort(my_sort)

print "\n".join(lines)
