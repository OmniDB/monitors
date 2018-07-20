from datetime import datetime
from random import randint

cpu_data = connection.Query('''
    create temporary table tabela (c1 text);
    copy tabela from program 'mpstat -P ALL 1 1 | grep "Average:" | tail -n +2 | tr -s " " | cut -f2,3 -d" "';
    select * from tabela;
''')

datasets = []
for cpu in cpu_data.Rows:
    if cpu!='':
        cpu_split = cpu[0].split(' ')
        color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
        datasets.append({
            "label": cpu_split[0],
            "fill": False,
            "backgroundColor": color,
            "borderColor": color,
            "lineTension": 0,
            "pointRadius": 1,
            "borderWidth": 1,
            "data": [cpu_split[1]]
        })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
