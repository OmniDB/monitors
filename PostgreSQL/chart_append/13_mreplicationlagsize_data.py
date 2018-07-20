from datetime import datetime
from random import randint

replags = connection.Query('''
    CREATE TEMPORARY TABLE omnidb_monitor_result (result1 TEXT, result2 TEXT);
    DO $$
    BEGIN
        IF current_setting('server_version_num')::integer < 100000 THEN
            EXECUTE 'INSERT INTO omnidb_monitor_result SELECT client_addr || ''-'' || application_name as standby,'
                    'round(pg_xlog_location_diff(pg_current_xlog_location(),replay_location)/1048576.0,2) as lag '
                    'FROM pg_stat_replication';
        ELSE
            EXECUTE 'INSERT INTO omnidb_monitor_result SELECT client_addr || ''-'' || application_name as standby,'
                'round(pg_wal_lsn_diff(pg_current_wal_lsn(),replay_lsn)/1048576.0,2) as lag '
                'FROM pg_stat_replication';
        END IF;
    END$$;
    SELECT result1 as standby, result2 as lag FROM omnidb_monitor_result;
''')

datasets = []
for replag in replags.Rows:
    color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
    datasets.append({
            "label": replag['standby'],
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
