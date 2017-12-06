from datetime import datetime
from random import randint

mem_data = connection.ExecuteScalar('''
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
    print subprocess.Popen("free -m | tail -n +2 | head -n 1 | tr -s ' ' | cut -f2,3,4 -d ' '", shell=True, stdout=subprocess.PIPE).stdout.read()
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
    result = codeOut.getvalue()
    plpy.execute("INSERT INTO omnidb_monitor_result VALUES ('{0}')".format(result))
    $$;
    SELECT * FROM omnidb_monitor_result;
''')

datasets = []
mem_split = mem_data.split(' ')
total_mem = mem_split[0]
used_mem = mem_split[1]
free_mem = mem_split[2]
perc_mem = round(int(used_mem)*100/int(total_mem),2)
color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
datasets.append({
        "label": "Memory",
        "fill": False,
        "backgroundColor": color,
        "borderColor": color,
        "lineTension": 0,
        "pointRadius": 1,
        "borderWidth": 1,
        "data": [perc_mem]
    })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
