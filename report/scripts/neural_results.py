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
    return r'%s - %s hidden units - %s iterations' % (model, num_hidden, epoch)


def echo_result(model, epoch, num_hidden):
    data = get_data(model, epoch, num_hidden)
    auc = np.array(data['auc'])
    low, high, _ = ci(auc)
    title = get_title(model, epoch, num_hidden)
    print r'\subsection{%s}' % (title,)
    echo_auc_table(auc, title)
    echo_statistics(auc)
    print ''
    print ''

def get_data(model, epoch, num_hidden):
    filename = '%s-%s-epochs-%s-hidden.json' % (model, epoch, num_hidden)
    with open(root+'/sessions/25-neural-network/data/'+filename) as f:
        data = json.load(f)
    return data


def walk(f):
    for model in ['inference-features', 'forward-selection']:
        for epoch, num_hidden in product([8,20], [3,5]):
            f(model, epoch, num_hidden)

def echo_all():
    walk(echo_result)

def echo_summary_table_row(model, epoch, hidden):
    translate = {
        'inference-features': 'W',
        'forward-selection': 'F'
    }
    data = get_data(model, epoch, hidden)
    auc = np.array(data['auc'])
    low, high, _ = ci(auc)
    print r'& %s %s hidden %s iter & \T\B %.04f & %.06f & [%.04f,%.04f]\\\cline{2-5}' % (translate[model], hidden, epoch, auc.mean(), auc.std(ddof=1), low, high)

def echo_logreg_rows():
    datafiles = [
        ('W', 'sessions/17-recreating-winning-entry/data/inference-features-for-report.json'),
        ('F top 3', 'sessions/18-forward-selection/data/top-3-features-for-report.json'),
        ('F all feat', 'sessions/18-forward-selection/data/all-features-for-report.json')
    ]
    for title, path in datafiles:
        data = json.load(open(path))
        auc = np.array(data['auc'])
        low, high, _ = ci(auc)
        print r'& %s & \T\B %.04f & %.06f & [%.04f,%.04f]\\\cline{2-5}' % (title, auc.mean(), auc.std(ddof=1), low, high)


def echo_summary_table_rows():
    walk(echo_summary_table_row)
    echo_logreg_rows()


if __name__ == '__main__':
    echo_logreg_rows()
