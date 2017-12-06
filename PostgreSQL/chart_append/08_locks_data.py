from datetime import datetime
from random import randint

locks = connection.Query('''
    SELECT mode,
           count(*) as count
    FROM pg_locks
    GROUP BY mode
''')

datasets = []
for lock in locks.Rows:
    color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
    datasets.append({
            "label": lock['mode'],
            "fill": False,
            "backgroundColor": color,
            "borderColor": color,
            "lineTension": 0,
            "pointRadius": 1,
            "borderWidth": 1,
            "data": [lock["count"]]
        })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
