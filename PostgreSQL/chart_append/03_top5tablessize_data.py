from datetime import datetime
from random import randint

tables = connection.Query('''
    SELECT nspname || '.' || relname AS relation,
           round(pg_relation_size(c.oid)/1048576.0,2) AS size
    FROM pg_class c
    LEFT JOIN pg_namespace n ON (n.oid = c.relnamespace)
    WHERE nspname NOT IN ('pg_catalog', 'information_schema')
      AND c.relkind <> 'i'
      AND nspname !~ '^pg_toast'
    ORDER BY pg_total_relation_size(c.oid) DESC
    LIMIT 5
''')

datasets = []
for table in tables.Rows:
    color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
    datasets.append({
            "label": table['relation'],
            "fill": False,
            "backgroundColor": color,
            "borderColor": color,
            "lineTension": 0,
            "pointRadius": 1,
            "borderWidth": 1,
            "data": [table["size"]]
        })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
