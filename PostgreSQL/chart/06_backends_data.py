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

data = []
color = []
label = []

for db in databases.Rows:
    data.append(db["numbackends"])
    color.append("rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")")
    label.append(db["datname"])

result = {
    "labels": label,
    "datasets": [
        {
            "data": data,
            "backgroundColor": color,
            "label": "Dataset 1"
        }
    ]
}
