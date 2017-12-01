from datetime import datetime

tables = connection.Query('''
    SELECT nspname || '.' || relname AS relation,
           round(pg_relation_size(c.oid)/1048576.0,2) AS size
    FROM pg_class c
    LEFT JOIN pg_namespace n ON (n.oid = c.relnamespace)
    WHERE nspname NOT IN ('pg_catalog', 'information_schema')
      AND c.relkind <> 'i'
      AND nspname !~ '^pg_toast'
    ORDER BY pg_total_relation_size(C.oid) DESC
    LIMIT 5
''')

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
for table in tables.Rows:
    datasets.append({
            "label": table['relation'],
            "fill": False,
            "backgroundColor": colors[color_index],
            "borderColor": colors[color_index],
            "lineTension": 0,
            "pointRadius": 1,
            "borderWidth": 1,
            "data": [table["size"]]
        })
    color_index = color_index + 1
    if color_index == len(colors):
        color_index = 0
