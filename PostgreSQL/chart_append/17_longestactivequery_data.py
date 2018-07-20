from datetime import datetime
from random import randint

duration = connection.ExecuteScalar('''
    SELECT duration FROM
    (SELECT EXTRACT(EPOCH FROM(now() - query_start))::INTEGER AS duration FROM pg_stat_activity WHERE state='active'
    UNION ALL
    SELECT 0) t
    WHERE duration is NOT NULL
    ORDER BY duration DESC
    LIMIT 1
''')

datasets = []
color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
datasets.append({
        "label": 'Query',
        "fill": False,
        "backgroundColor": color,
        "borderColor": color,
        "lineTension": 0,
        "pointRadius": 1,
        "borderWidth": 1,
        "data": [duration]
    })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
