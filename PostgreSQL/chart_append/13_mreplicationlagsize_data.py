from datetime import datetime
from random import randint

replags = connection.Query('''
    SELECT client_addr || '-' || application_name as standby,
           round(pg_xlog_location_diff(pg_current_xlog_location(),replay_location)/1048576.0,2) AS lag
    FROM pg_stat_replication
''')

datasets = []
for replag in replags.Rows:
    color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
    datasets.append({
            "label": replag['standby'],
            "fill": False,
            "backgroundColor": color,
            "borderColor": color,
            "lineTension": 0,
            "pointRadius": 1,
            "borderWidth": 1,
            "data": [replag['lag']]
        })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
