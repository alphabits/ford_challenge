import json


with open('sessions/17-recreating-winning-entry/data/inference-features-10-fold-cv-report.json', 'r') as f:
    data = json.load(f)

print r'\begin{tabularx}{\textwidth}{ l R R R R R }'
print r'Run & sdE5 & V11 & E9 & Intercept & AUC \\\hline'
        
w = data['weights']
auc = data['auc']
b = data['intercepts']

for i in range(len(data['weights'])):
    print r'%s & %.04f & %.04f & %.04f & %.04f & %.04f \\' % (i+1, w[i][0], w[i][1], w[i][2], b[i], auc[i])

print r'\end{tabularx}'
