data = connection.Query('''
    SELECT pg_is_in_recovery() as "In recovery"
''')

result = {
    "columns": data.Columns,
    "data": data.Rows
}
