from datetime import datetime

tables = connection.Query('''
    SELECT z.schemaname || '.' || z.tablename as relation, sum_wasted/1048576.0 AS size
    FROM (
    SELECT y.schemaname, y.tablename, y.current_database, wastedbytes + sum(wastedibytes)::bigint AS sum_wasted
    FROM (
    SELECT current_database,schemaname, tablename, tbloat, wastedbytes, iname, ibloat, wastedibytes AS wastedibytes
    FROM (
    SELECT
      current_database(), schemaname, tablename, /*reltuples::bigint, relpages::bigint, otta,*/
      ROUND((CASE WHEN otta=0 THEN 0.0 ELSE sml.relpages::FLOAT/otta END)::NUMERIC,1) AS tbloat,
      CASE WHEN relpages < otta THEN 0 ELSE bs*(sml.relpages-otta)::BIGINT END AS wastedbytes,
      iname, /*ituples::bigint, ipages::bigint, iotta,*/
      ROUND((CASE WHEN iotta=0 OR ipages=0 THEN 0.0 ELSE ipages::FLOAT/iotta END)::NUMERIC,1) AS ibloat,
      CASE WHEN ipages < iotta THEN 0 ELSE bs*(ipages-iotta) END AS wastedibytes
    FROM (
      SELECT
        schemaname, tablename, cc.reltuples, cc.relpages, bs,
        CEIL((cc.reltuples*((datahdr+ma-
          (CASE WHEN datahdr%ma=0 THEN ma ELSE datahdr%ma END))+nullhdr2+4))/(bs-20::FLOAT)) AS otta,
        COALESCE(c2.relname,'?') AS iname, COALESCE(c2.reltuples,0) AS ituples, COALESCE(c2.relpages,0) AS ipages,
        COALESCE(CEIL((c2.reltuples*(datahdr-12))/(bs-20::FLOAT)),0) AS iotta -- very rough approximation, assumes all cols
      FROM (
        SELECT
          ma,bs,schemaname,tablename,
          (datawidth+(hdr+ma-(CASE WHEN hdr%ma=0 THEN ma ELSE hdr%ma END)))::NUMERIC AS datahdr,
          (maxfracsum*(nullhdr+ma-(CASE WHEN nullhdr%ma=0 THEN ma ELSE nullhdr%ma END))) AS nullhdr2
        FROM (
          SELECT
            schemaname, tablename, hdr, ma, bs,
            SUM((1-null_frac)*avg_width) AS datawidth,
            MAX(null_frac) AS maxfracsum,
            hdr+(
              SELECT 1+COUNT(*)/8
              FROM pg_stats s2
              WHERE null_frac<>0 AND s2.schemaname = s.schemaname AND s2.tablename = s.tablename
            ) AS nullhdr
          FROM pg_stats s, (
            SELECT
              (SELECT current_setting('block_size')::NUMERIC) AS bs,
              CASE WHEN SUBSTRING(v,12,3) IN ('8.0','8.1','8.2') THEN 27 ELSE 23 END AS hdr,
              CASE WHEN v ~ 'mingw32' THEN 8 ELSE 4 END AS ma
            FROM (SELECT version() AS v) AS foo
          ) AS constants
          GROUP BY 1,2,3,4,5
        ) AS foo
      ) AS rs
      JOIN pg_class cc ON cc.relname = rs.tablename
      JOIN pg_namespace nn ON cc.relnamespace = nn.oid AND nn.nspname = rs.schemaname AND nn.nspname <> 'information_schema'
      LEFT JOIN pg_index i ON indrelid = cc.oid
      LEFT JOIN pg_class c2 ON c2.oid = i.indexrelid
    ) AS sml) x) y
    GROUP BY y.schemaname, y.tablename, y.current_database, y.wastedbytes) z
    ORDER BY z.sum_wasted DESC
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
