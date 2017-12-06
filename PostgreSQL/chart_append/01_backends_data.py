from datetime import datetime
from random import randint

databases = connection.Query('''
    SELECT d.datname,
           s.numbackends
    FROM pg_stat_database s
    INNER JOIN pg_database d
    ON d.oid = s.datid
    WHERE NOT d.datistemplate
''')

datasets = []
for db in databases.Rows:
    color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
    datasets.append({
            "label": db['datname'],
            "fill": False,
            "backgroundColor": color,
            "borderColor": color,
            "lineTension": 0,
            "pointRadius": 1,
            "borderWidth": 1,
            "data": [db["numbackends"]]
        })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
