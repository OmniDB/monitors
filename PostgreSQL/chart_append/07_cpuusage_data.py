from datetime import datetime
from random import randint

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

datasets = []
for cpu in cpu_data.split('\n'):
    if cpu!='':
        cpu_split = cpu.split(' ')
        color = "rgb(" + str(randint(125, 225)) + "," + str(randint(125, 225)) + "," + str(randint(125, 225)) + ")"
        datasets.append({
            "label": cpu_split[0],
            "fill": False,
            "backgroundColor": color,
            "borderColor": color,
            "lineTension": 0,
            "pointRadius": 1,
            "borderWidth": 1,
            "data": [cpu_split[1]]
        })

result = {
    "labels": [datetime.now().strftime('%H:%M:%S')],
    "datasets": datasets
}
