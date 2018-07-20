from datetime import datetime
from random import randint

replags = connection.Query('''
    CREATE TEMPORARY TABLE omnidb_monitor_result (result TEXT);
    DO $$DECLARE r record;
    BEGIN
        IF current_setting('server_version_num')::integer < 100000 THEN
            EXECUTE 'INSERT INTO omnidb_monitor_result '
                    'SELECT round(pg_xlog_location_diff(pg_last_xlog_receive_location(), pg_last_xlog_replay_location())/1048576.0,2) AS lag';
        ELSE
            EXECUTE 'INSERT INTO omnidb_monitor_result '
                    'SELECT round(pg_wal_lsn_diff(pg_last_wal_receive_lsn(), pg_last_wal_replay_lsn())/1048576.0,2) AS lag';
        END IF;
    END$$;
    SELECT result as lag FROM omnidb_monitor_result;
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
