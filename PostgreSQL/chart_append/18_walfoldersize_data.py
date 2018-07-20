from datetime import datetime
from random import randint

size = connection.ExecuteScalar('''
    CREATE TEMPORARY TABLE omnidb_temp (c1 TEXT, c2 TEXT);
    COPY omnidb_temp FROM PROGRAM 'du -s pg_xlog || du -s pg_wal';
    SELECT ROUND(c1::BIGINT/1048576.0,2) AS pg_xlog_size FROM omnidb_temp;
''')

datasets = []
color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
datasets.append({
        "label": 'WAL Folder Size',
        "fill": False,
        "backgroundColor": color,
        "borderColor": color,
        "lineTension": 0,
        "pointRadius": 1,
        "borderWidth": 1,
        "data": [size]
    })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
