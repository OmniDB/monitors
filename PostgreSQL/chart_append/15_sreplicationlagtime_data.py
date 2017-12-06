from datetime import datetime
from random import randint

replags = connection.Query('''
    SELECT COALESCE(ROUND(EXTRACT(epoch FROM now() - pg_last_xact_replay_timestamp())),0) AS lag
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
