from datetime import datetime
from random import randint

databases = connection.Query('''
    SELECT d.datname AS datname,
           round(pg_catalog.pg_database_size(d.datname)/1048576.0,2) AS size
    FROM pg_catalog.pg_database d
    WHERE d.datname not in ('template0','template1')
''')

data = []
color = []
label = []

for db in databases.Rows:
    data.append(db["size"])
    color.append("rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")")
    label.append(db["datname"])

total_size = connection.ExecuteScalar('''
    SELECT round(sum(pg_catalog.pg_database_size(datname)/1048576.0),2)
    FROM pg_catalog.pg_database
    WHERE NOT datistemplate
''')

result = {
    "labels": label,
    "datasets": [
        {
            "data": data,
            "backgroundColor": color,
            "label": "Dataset 1"
        }
    ],
    "title": "Database Size (Total: " + str(total_size) + " MB)"
}
