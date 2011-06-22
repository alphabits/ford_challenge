import json
from itertools import product
import numpy as np

from src.utils2 import confidence_interval_t_distribution as ci, get_path


root = get_path(__file__) + '/../..'


def get_table_content(auc):
    lines = []
    l = len(auc)
    for i, score in enumerate(auc):
        append = '' if i+1 < l else r'\hline'
        lines.append(r'%s & %.04f \\%s' % (i+1, score, append))
    return '\n'.join(lines)

def echo_auc_table(auc, title):
    table_content = get_table_content(auc)
    print r'''\begin{table}
    \centering
    {\sffamily\small
        \begin{tabularx}{30mm}{ l R }
            Run & AUC \\\hline
            %s
        \end{tabularx}
    }
    \caption{%s}
\end{table} ''' % (table_content, title)


def echo_statistics(auc):
    m = auc.mean()
    std = auc.std(ddof=1)
    low, high, _ = ci(auc)
    print r'''\subsubsection{Statistics on the AUC-score}
First the sample mean and sample standard deviation are calculated
\[
    m = %.04f \quad\quad\text{and}\quad\quad s = %.06f
\]
which gives the 95\%% confidence interval
\[
    \CI{%.04f}{%.04f}
\]''' % (m, std, low, high)


def get_title(model, epoch, num_hidden):
    return r'%s - %s hidden units - %s iterations' % (model, epoch, num_hidden)



for model in ['inference-features', 'forward-selection']:
    for epoch, num_hidden in product([8,20], [3,5]):
        filename = '%s-%s-epochs-%s-hidden.json' % (model, epoch, num_hidden)
        with open(root+'/sessions/25-neural-network/data/'+filename) as f:
            data = json.load(f)
        auc = np.array(data['auc'])
        low, high, _ = ci(auc)
        title = get_title(model, epoch, num_hidden)
        print r'\subsection{%s}' % (title,)
        echo_auc_table(auc, title)
        echo_statistics(auc)
        print ''
        print ''
