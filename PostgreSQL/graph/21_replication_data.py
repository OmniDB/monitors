from datetime import datetime
from random import randint

nodes = []
edges = []

try:
    repl_nodes = connection.Query('''
    select application_name,
           pg_size_pretty(pg_wal_lsn_diff(pg_current_wal_lsn(),coalesce(replay_lsn,flush_lsn))) lag_size
    from pg_stat_replication
    ''')
except:
    repl_nodes = connection.Query('''
    select application_name,
           pg_size_pretty(pg_xlog_location_diff(pg_current_xlog_location(),coalesce(replay_location,flush_location)) lag_size
    from pg_stat_replication
    ''')

if len(repl_nodes.Rows) == 0:
    raise Exception('There are no nodes replicating from this instance.')

nodes.append({
            "data": {
                "id": 'local',
                "label": 'local',
            },
            "classes": 'node_local'
        })

for repl_node in repl_nodes.Rows:
    nodes.append({
            "data": {
                "id": 'node_' + repl_node['application_name'],
                "label": repl_node['application_name']
            },
            "classes": 'node_remote'
        })
    edges.append({
            "data": {
                "id": 'edge_' + repl_node['application_name'],
                "label": repl_node['lag_size'],
                "source": 'local',
                "target": 'node_' + repl_node['application_name']
            }
        })

result = {
    "nodes": nodes,
    "edges": edges
}
