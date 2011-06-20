import json

from src.utils2 import get_path

path = get_path(__file__)+'/../..'
#json_path = path+'/sessions/18-forward-selection/data/all-features-auc-score-10-bins.json'
json_path = path+'/sessions/18-forward-selection/data/top-3-features-auc-score-10-bins.json'


with open(json_path, 'r') as f:
    data = json.load(f)

auc_list = data['auc']

print r'\begin{tabularx}{30mm}{ l R }'
print r'Run & AUC \\\hline'

for i, auc in enumerate(auc_list):
    line = r'\hline' if (i+1)==len(auc_list) else ''
    print r'%s & %.04f \\%s' % (i+1, auc, line)

print r'\end{tabularx}'
