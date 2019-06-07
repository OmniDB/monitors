from datetime import datetime
from random import randint

try:
    if previous_data != None:
        query = "select round(pg_wal_lsn_diff(pg_current_wal_lsn(),'" + previous_data["current_lsn"] + "')/(1048576*extract(epoch from now()::time - '" + previous_data["current_time"] + "'::time))::numeric,2) as wal_rate, pg_current_wal_lsn() as current_lsn, now()::time as current_time"
    else:
        query = 'select 0 as wal_rate, pg_current_wal_lsn() as current_lsn, now()::time as current_time'
    query_data = connection.Query(query)
except:
    if previous_data != None:
        query = "select round(pg_xlog_location_diff(pg_current_xlog_location(),'" + previous_data["current_lsn"] + "')/(1048576*extract(epoch from now()::time - '" + previous_data["current_time"] + "'::time))::numeric,2) as wal_rate, pg_current_xlog_location() as current_lsn, now()::time as current_time"
    else:
        query = 'select 0 as wal_rate, pg_current_xlog_location() as current_lsn, now()::time as current_time'
    query_data = connection.Query(query)

datasets = []
color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
datasets.append({
        "label": 'Rate',
        "fill": False,
        "backgroundColor": color,
        "borderColor": color,
        "lineTension": 0,
        "pointRadius": 1,
        "borderWidth": 1,
        "data": [query_data.Rows[0]['wal_rate']]
    })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets,
    "current_lsn": query_data.Rows[0]['current_lsn'],
    'current_time': query_data.Rows[0]['current_time']
}
