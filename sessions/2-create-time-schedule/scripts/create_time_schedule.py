# -*- coding: utf-8 -*-

schedule = [
    ['**Idefasen**', []],
    ['Projektbeskrivelse', [1]],
    ['Vejlederaftaler', [1]],
    ['Problemformulering', [1]],
    ['Litteratursøgning', [1,2]],
    ['**Projektarbejde**', []],
    ['Teoritilegnelse', range(2,11)],
    ['Indledende datavisualisering', [4,5]],
    ['Skrive indledning + teoriafsnit', [4,5]],
    ['Fjern outliers + udvælg features', [4,5]],
    ['Klassifikation (uddybes senere)', range(5,12)],
    ['Opsamlende databehandling + plot til rapporten', [11,12]],
    ['Vejledermøder', range(4,16)],
    ['Skrivning af logbog', range(3,17)],
    ['Rapportskrivning', [12,13,14,15]],
    ['Udarbejde præsentation', [15,16]],
    ['**Evaluering**', []],
    ['Fremlæggelse og forsvar', [16]],
    ['Evaluering', [16]],
    ['Øl og hornmusik', [16]]
]

num_weeks = 16

widths = ['20'] + num_weeks*['5']

header = ['"Opgave"']

for i in range(1, num_weeks+1):
    header.append('"Uge %s"' % (i,))

print '    :header: %s' % (','.join(header),)
print '    :widths: %s' % (','.join(widths),)
print ''

for j in range(len(schedule)):
    title, weeks = schedule[j]
    week_texts = []
    for k in range(1, num_weeks+1):
        symbol = '"X"' if k in weeks else '""'
        week_texts.append(symbol)
    print '    "%s",%s' % (title,','.join(week_texts))
