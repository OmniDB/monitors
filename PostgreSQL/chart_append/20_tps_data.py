from datetime import datetime
from random import randint

if previous_data != None:
    query = "select round((sum(xact_commit+xact_rollback) - " + previous_data["current_count"] + ")/(extract(epoch from now()::time - '" + previous_data["current_time"] + "'::time))::numeric,2) as tps, sum(xact_commit+xact_rollback) as current_count, now()::time as current_time FROM pg_stat_database"
else:
    query = 'select 0 as tps, sum(xact_commit+xact_rollback) as current_count, now()::time as current_time FROM pg_stat_database'

query_data = connection.Query(query)

datasets = []
color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
datasets.append({
        "label": 'Rate',
        "fill": False,
        "backgroundColor": color,
        "borderColor": color,
        "lineTension": 0,
        "pointRadius": 0,
        "borderWidth": 1,
        "data": [query_data.Rows[0]['tps']]
    })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets,
    "current_count": query_data.Rows[0]['current_count'],
    'current_time': query_data.Rows[0]['current_time']
}
