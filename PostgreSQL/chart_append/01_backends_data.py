from datetime import datetime

databases = connection.Query('''
    SELECT datname,
           numbackends,
           now() AS time
    FROM pg_stat_database
    WHERE datname NOT IN ('template0','template1')
''')

max_connections = connection.ExecuteScalar('show max_connections')

colors = [
"rgb(255, 99, 132)",
"rgb(255, 159, 64)",
"rgb(255, 205, 86)",
"rgb(75, 192, 192)",
"rgb(54, 162, 235)",
"rgb(153, 102, 255)",
"rgb(201, 203, 207)"]

datasets = []
color_index = 0
for db in databases.Rows:
    datasets.append({
            "label": db['datname'],
            "fill": False,
            "backgroundColor": colors[color_index],
            "borderColor": colors[color_index],
            "lineTension": 0,
            "pointRadius": 1,
            "borderWidth": 1,
            "data": [db["numbackends"]]
        })
    color_index = color_index + 1
    if color_index == len(colors):
        color_index = 0
