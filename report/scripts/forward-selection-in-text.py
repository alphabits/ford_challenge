import json

from src.utils2 import get_path


root = get_path(__file__) + '/../..'
with open(root+'/sessions/18-forward-selection/data/forward-selection-results-2-for-docs.json') as f:
    data = json.load(f)


def print_table_header():
    print r'\begin{tabularx}{40mm}{ l R }'
    print r'Feature added & AUC \\\hline'

def print_table_footer():
    print r'\end{tabularx}'

features = data['labels_chosen'][:5] + data['labels_chosen'][-2:]
aucs = data['max_auc'][:5] + data['max_auc'][-2:]

print_table_header()
for i, feature in enumerate(features):
    print r'%s & %.04f \\' % (feature, aucs[i])
    if i==4:
        print r'$\vdots$ & $\vdots$ \\'
print_table_footer()
