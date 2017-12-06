from datetime import datetime

data = connection.Query('''
    SELECT *
    FROM pg_stat_activity
''')

result = {
    "columns": data.Columns,
    "data": data.Rows
}
