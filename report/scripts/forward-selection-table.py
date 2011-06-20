import json

from src.utils2 import get_path


root = get_path(__file__) + '/../..'
with open(root+'/sessions/18-forward-selection/data/forward-selection-results-2-for-docs.json') as f:
    data = json.load(f)

num_rows = len(data['labels_chosen'])
columns_change = int(num_rows/2)

def print_table_header():
    print r'\begin{minipage}[t]{50mm}'
    print r'\vspace{0pt}'
    print r'\begin{tabularx}{50mm}{ l R }'
    print r'Feature added & AUC \\\hline'

def print_table_footer():
    print r'\end{tabularx}'
    print r'\end{minipage}'

print_table_header()

for i, feature in enumerate(data['labels_chosen']):
    if i==columns_change:
        print r'{\itshape continues ...} & '
        print_table_footer()
        print r'\hspace{15mm}'
        print_table_header()
        print r'{\itshape ... continued} & \\'
    print r'%s & %.04f \\' % (feature, data['max_auc'][i])

print_table_footer()
