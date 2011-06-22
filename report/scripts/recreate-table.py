import json


with open('sessions/17-recreating-winning-entry/data/inference-features-for-report.json', 'r') as f:
    data = json.load(f)

print r'\begin{tabularx}{40mm}{ l R }'
print r'Run & AUC \\\hline'
        
auc = data['auc']

for i in range(len(data['auc'])):
    print r'%s & %.04f \\' % (i+1, auc[i])

print r'\end{tabularx}'
