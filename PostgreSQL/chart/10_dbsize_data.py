from datetime import datetime

databases = connection.Query('''
    SELECT d.datname AS datname,
           round(pg_catalog.pg_database_size(d.datname)/1048576.0,2) AS size
    FROM pg_catalog.pg_database d
    WHERE d.datname not in ('template0','template1')
''')

total_size = connection.ExecuteScalar('''
    SELECT round(sum(pg_catalog.pg_database_size(d.datname)/1048576.0),2)
    FROM pg_catalog.pg_database d
    WHERE d.datname not in ('template0','template1')
''')

colors = [
"rgb(255, 99, 132)",
"rgb(255, 159, 64)",
"rgb(255, 205, 86)",
"rgb(75, 192, 192)",
"rgb(54, 162, 235)",
"rgb(153, 102, 255)",
"rgb(201, 203, 207)"]

data = []
color = []
label = []

color_index = 0

for db in databases.Rows:
    data.append(db["size"])
    color.append(colors[color_index])
    label.append(db["datname"])
    color_index = color_index + 1
    if color_index == len(colors):
        color_index = 0
        
