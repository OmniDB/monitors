from datetime import datetime

cpu_data = connection.ExecuteScalar('''
    CREATE TEMPORARY TABLE omnidb_monitor_result (result TEXT);
    DO LANGUAGE plpythonu
    $$
    import sys
    import StringIO
    import subprocess
    codeOut = StringIO.StringIO()
    codeErr = StringIO.StringIO()
    sys.stdout = codeOut
    sys.stderr = codeErr
    print subprocess.Popen("mpstat -P ALL 1 1 | grep 'Average:' | tail -n +2 | tr -s ' ' | cut -f2,3 -d' '", shell=True, stdout=subprocess.PIPE).stdout.read()
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    result = codeOut.getvalue()
    plpy.execute("INSERT INTO omnidb_monitor_result VALUES ('{0}')".format(result))
    $$;
    SELECT * FROM omnidb_monitor_result;
''')

colors = [
"rgb(255, 99, 132)",
"rgb(255, 159, 64)",
"rgb(255, 205, 86)",
"rgb(75, 192, 192)",
"rgb(54, 162, 235)",
"rgb(153, 102, 255)",
"rgb(201, 203, 207)"]

cpu_list = []
color_index = 0
for cpu in cpu_data.split('\n'):
    if cpu!='':
        cpu_split = cpu.split(' ')
        cpu_list.append({
            "label": cpu_split[0],
            "fill": False,
            "backgroundColor": colors[color_index],
            "borderColor": colors[color_index],
            "lineTension": 0,
            "pointRadius": 1,
            "borderWidth": 1,
            "data": [cpu_split[1]]
        })
        color_index = color_index + 1
        if color_index == len(colors):
            color_index = 0
