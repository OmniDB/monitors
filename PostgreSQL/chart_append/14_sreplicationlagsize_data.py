from datetime import datetime
from random import randint

replags = connection.Query('''
    SELECT round(pg_xlog_location_diff(pg_last_xlog_receive_location(), pg_last_xlog_replay_location())/1048576.0,2) AS lag
''')

datasets = []
for replag in replags.Rows:
    color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
    datasets.append({
            "label": "Lag",
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
