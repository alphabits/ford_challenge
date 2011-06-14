from __future__ import with_statement
import json


def render(filter_keys=None):
    with open('../sessions/9-data-exploration/src/unique_values_combined.json', 'r') as f:
        data = json.load(f)
    print r'\begin{tabularx}{\textwidth}{ X | R R R }'
    print r'Feature & Min in trial & Max in trial & Whole dataset \\\hline'
    for k in sorted(data.keys()):
        if filter_keys and k in filter_keys:
            continue
        tmpdata = data[k]
        tmpdata['key'] = k
        print r'%(key)s &  %(min_pr_trial)d & %(max_pr_trial)d & %(all_data)d \\' % tmpdata
    print r'\end{tabularx}'

if __name__ == '__main__':
    render()
