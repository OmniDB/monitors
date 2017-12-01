result = {
    "type": "line",
    "data": {
        "labels": [datetime.now().strftime('%H:%M:%S')],
        "datasets": cpu_list
    },
    "options": {
        "responsive": True,
        "title":{
            "display":True,
            "text":"CPU usage"
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
                    "labelString": "Value",
                },
                "ticks": {
                    "beginAtZero": True,
                    "max": 100
                }
            }]
        }
    }
}
