import os

from src.utils import get_path


sess_root = get_path(__file__) + '/..'

lines = []
for f in os.listdir(sess_root):
    if f[0]!='t' and f.endswith('rst') and not f.startswith('index'):
        (f_str, ext) = f.split('.')
        lines.append(f_str)

lines.sort()
print "\n".join(lines)
