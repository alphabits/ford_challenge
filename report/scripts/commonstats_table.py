from __future__ import with_statement
import json


def render(path, filter_keys=None):
    with open(path, 'r') as f:
        data = json.load(f)
    print r'\begin{tabularx}{\textwidth}{ X | R R R R }'
    print r'Feature & Mean & Min & Max & Std.Dev \\\hline'
    for k in sorted(data.keys()):
        if filter_keys and k not in filter_keys:
            continue
        tmpdata = data[k]
        tmpdata['key'] = k
        print r'%(key)s & %(mean).2f & %(min).2f & %(max).2f & %(std).2f \\' % tmpdata
    print r'\end{tabularx}'

if __name__ == '__main__':
    render('../sessions/9-data-exploration/src/summary_statistics.json')
