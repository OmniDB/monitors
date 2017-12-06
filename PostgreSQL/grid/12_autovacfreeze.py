from datetime import datetime

data = connection.Query('''
    SELECT relname as table_name,
           pg_size_pretty(pg_table_size(oid)) as table_size,
           age(relfrozenxid) as xid_age,
           current_setting('autovacuum_freeze_max_age')::integer as max_age,
           round(age(relfrozenxid)/(current_setting('autovacuum_freeze_max_age')::integer)::numeric*100.0,4) as perc
    FROM pg_class
    WHERE relkind in ('r', 't')
    ORDER BY age(relfrozenxid) DESC
    LIMIT 20;
''')

result = {
    "columns": data.Columns,
    "data": data.Rows
}
