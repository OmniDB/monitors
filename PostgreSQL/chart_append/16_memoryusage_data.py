from datetime import datetime
from random import randint

try:
    mem_data = connection.ExecuteScalar('''
        create temporary table tabela (c1 text);
        copy tabela from program 'free -m | tail -n +2 | head -n 1 | tr -s " " | cut -f2,3,4 -d " "';
        select * from tabela;
    ''')
except:
    raise Exception('This chart can not be executed in a standby server.')

if mem_data is None:
    raise Exception('This chart can only be executed in a Linux server.')

datasets = []
mem_split = mem_data.split(' ')
total_mem = mem_split[0]
used_mem = mem_split[1]
free_mem = mem_split[2]
perc_mem = round(int(used_mem)*100/int(total_mem),2)
color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
datasets.append({
        "label": "Memory",
        "fill": False,
        "backgroundColor": color,
        "borderColor": color,
        "lineTension": 0,
        "pointRadius": 1,
        "borderWidth": 1,
        "data": [perc_mem]
    })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
