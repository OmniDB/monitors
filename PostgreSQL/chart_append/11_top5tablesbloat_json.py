result = {
    "type": "line",
    "data": {
        "labels": [datetime.now().strftime('%H:%M:%S')],
        "datasets": datasets
    },
    "options": {
        "responsive": True,
        "title":{
            "display":True,
            "text":"Bloat: top 5 tables"
        },
        "tooltips": {
            "mode": "index",
            "intersect": False
        },
        "hover": {
            "mode": "nearest",
            "intersect": True
        },
        "scales": {
            "xAxes": [{
                "display": True,
                "scaleLabel": {
                    "display": True,
                    "labelString": "Time"
                }
            }],
            "yAxes": [{
                "display": True,
                "scaleLabel": {
                    "display": True,
                    "labelString": "Size (MB)"
                }
            }]
        }
    }
}
